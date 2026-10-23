"""Small OpenAI (GPT) helper shared by the agents: one JSON answer, with model fallbacks.

GPT is a second, independent opinion next to Claude. It must never stop an agent: callers catch GPTError
and carry on without it.
"""
import json
import os
import re
import time

import requests

API = "https://api.openai.com/v1"


class GPTError(RuntimeError):
    pass


def available() -> bool:
    return bool(os.environ.get("OPENAI_API_KEY", "").strip())


def _text_from_responses(data: dict) -> str:
    if data.get("output_text"):
        return data["output_text"]
    parts = []
    for item in data.get("output", []):
        for c in item.get("content", []) or []:
            if c.get("type") in ("output_text", "text") and c.get("text"):
                parts.append(c["text"])
    return "".join(parts)


def _parse(text: str) -> dict:
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", (text or "").strip())
    return json.loads(text[text.find("{"): text.rfind("}") + 1])


def _err(r) -> str:
    try:
        e = r.json().get("error", {})
        return f"{r.status_code} {e.get('code') or e.get('type') or ''}: {e.get('message', '')}"[:400]
    except ValueError:
        return f"{r.status_code}: {r.text[:300]}"


def ask_json(system: str, user: str, models: list[str] | str, max_tokens: int = 3000,
             timeout: int = 180) -> tuple[dict, str]:
    """Returns (json answer, model used). Tries each model in order; Responses API first, then Chat Completions."""
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise GPTError("OPENAI_API_KEY is not set")
    hdr = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    models = [models] if isinstance(models, str) else list(models)
    errors = []
    for m in models:
        for attempt in range(2):
            try:
                r = requests.post(f"{API}/responses", headers=hdr, timeout=timeout, json={
                    "model": m, "instructions": system, "input": user, "max_output_tokens": max_tokens,
                    "text": {"format": {"type": "json_object"}}})
                if r.status_code == 200:
                    return _parse(_text_from_responses(r.json())), m
                msg = _err(r)
                if r.status_code == 404 and "model" not in msg.lower():  # no Responses API -> Chat Completions
                    r = requests.post(f"{API}/chat/completions", headers=hdr, timeout=timeout, json={
                        "model": m, "max_completion_tokens": max_tokens,
                        "response_format": {"type": "json_object"},
                        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]})
                    if r.status_code == 200:
                        return _parse(r.json()["choices"][0]["message"]["content"]), m
                    msg = _err(r)
                low = msg.lower()
                if r.status_code in (401, 403) or "quota" in low or "billing" in low:
                    raise GPTError(f"OpenAI account problem: {msg}")
                errors.append(f"{m}: {msg}")
                if r.status_code in (400, 404) and "model" in low:
                    break  # this model is not available -> next model
            except GPTError:
                raise
            except (requests.RequestException, ValueError, KeyError) as e:
                errors.append(f"{m}: {type(e).__name__}: {e}"[:300])
            time.sleep(3 * (attempt + 1))
    raise GPTError("GPT did not answer: " + " | ".join(errors)[-700:])
