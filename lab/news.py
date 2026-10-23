"""Reads world, war/geopolitics and economy headlines and asks Claude what they mean for gold."""
import datetime as dt
import email.utils
import html
import json
import re
import xml.etree.ElementTree as ET

import anthropic
import requests

PROMPT = """You are a cautious macro analyst. Below are the latest headlines (newest first) about geopolitics,
wars, central banks, inflation, the US dollar and gold. Judge the likely effect on the GOLD price over the
next 1-4 hours.

Think about: safe-haven demand (wars, escalation, crises), real interest rates and Fed expectations
(hawkish = bearish gold, dovish = bullish), US dollar strength (strong dollar = bearish gold), inflation surprises,
central bank gold buying. Old, already-priced-in or contradictory news should LOWER your confidence.
If nothing important happened, score near 0.

Headlines (lines starting with NEW arrived since your last analysis; weigh them most):
{headlines}

Call the submit tool with JSON:
{{"score": number from -1 (strongly bearish) to 1 (strongly bullish),
  "confidence": number from 0 to 1,
  "reason": "one or two sentences, written in TURKISH",
  "key_events": ["max 3 short items, in Turkish"]}}"""


def headlines(feeds: list[str], max_age_hours: float = 8, limit: int = 45) -> list[str]:
    now = dt.datetime.now(dt.timezone.utc)
    items, seen = [], set()
    for url in feeds:
        try:
            r = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0 trade-lab"})
            root = ET.fromstring(r.content)
        except Exception:  # noqa: BLE001 one broken feed must not stop the bot
            continue
        for it in root.iter("item"):
            title = html.unescape((it.findtext("title") or "").strip())
            pub = it.findtext("pubDate")
            try:
                when = email.utils.parsedate_to_datetime(pub) if pub else now
            except (TypeError, ValueError):
                when = now
            if when.tzinfo is None:
                when = when.replace(tzinfo=dt.timezone.utc)
            age = (now - when).total_seconds() / 3600
            key = re.sub(r"\W+", " ", title.lower())[:80]
            if title and age <= max_age_hours and key not in seen:
                seen.add(key)
                items.append((when, title))
    items.sort(key=lambda x: x[0], reverse=True)
    return [f"[{w.strftime('%H:%M')} UTC] {t}" for w, t in items[:limit]]


def gold_sentiment(api_key: str, model: str, feeds: list[str], lines: list[str] | None = None,
                   new_lines: list[str] | None = None) -> dict:
    lines = lines if lines is not None else headlines(feeds)
    if new_lines:  # point Claude at what just arrived
        lines = [("NEW " + x if x in set(new_lines) else x) for x in lines]
    if not lines:
        return {"score": 0.0, "confidence": 0.0, "reason": "no fresh headlines", "key_events": [], "n": 0}
    client = anthropic.Anthropic(api_key=api_key)
    tool = {"name": "submit", "description": "Submit the analysis.",
            "input_schema": {"type": "object", "properties": {
                "score": {"type": "number"}, "confidence": {"type": "number"},
                "reason": {"type": "string"}, "key_events": {"type": "array", "items": {"type": "string"}}},
                "required": ["score", "confidence", "reason"]}}
    msg = client.messages.create(model=model, max_tokens=600, tools=[tool],
                                 messages=[{"role": "user", "content": PROMPT.format(headlines="\n".join(lines))}])
    out = None
    for b in msg.content:
        if b.type == "tool_use":
            out = dict(b.input)
    if out is None:
        text = "".join(getattr(b, "text", "") for b in msg.content)
        out = json.loads(text[text.find("{"): text.rfind("}") + 1])
    out["score"] = max(-1.0, min(1.0, float(out.get("score", 0))))
    out["confidence"] = max(0.0, min(1.0, float(out.get("confidence", 0))))
    out["n"] = len(lines)
    return out


def gpt_sentiment(models, lines: list[str], new_lines: list[str] | None = None) -> dict:
    """Same headlines, same question, answered independently by GPT (OpenAI). Raises gpt.GPTError on failure."""
    import gpt
    if new_lines:
        lines = [("NEW " + x if x in set(new_lines) else x) for x in lines]
    if not lines:
        return {"score": 0.0, "confidence": 0.0, "reason": "no fresh headlines", "key_events": []}
    prompt = PROMPT.format(headlines="\n".join(lines)).replace("Call the submit tool with JSON:", "Answer with JSON:")
    out, used = gpt.ask_json("You are a cautious macro analyst. Answer with a single JSON object.", prompt, models,
                             max_tokens=800, timeout=90)
    return {"score": max(-1.0, min(1.0, float(out.get("score", 0)))),
            "confidence": max(0.0, min(1.0, float(out.get("confidence", 0)))),
            "reason": str(out.get("reason", ""))[:300], "key_events": out.get("key_events", [])[:3], "model": used}
