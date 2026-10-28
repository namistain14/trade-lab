"""Jarvis usage meter. Loaded automatically by Python when this folder is on PYTHONPATH (workflow env).

Watches HTTP responses from paid AI services (Anthropic, OpenAI, ElevenLabs, Kling) made with `requests` or
`httpx` (the Anthropic / OpenAI SDKs), and at process exit prints ONE line to the job log:
    JARVIS_USAGE {"v":1,"items":[...]}
Jarvis reads the job log, prices the items and shows the spend per agent / content.
Only counts (tokens, characters, credits, units, model names) are recorded — never prompts, answers, keys or files.
It never changes a request or a response; any error here is swallowed so the real job is never affected.
Same file in namistain-ops, vumeloo-agent and trade-lab (keep them identical).
"""
import atexit
import json
import os
import sys

_items: list = []
_seen_tasks: set = set()
_MAX = 4000


def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def _body_json(raw):
    if not raw:
        return None
    try:
        if isinstance(raw, (bytes, bytearray)):
            if len(raw) > 2_000_000 or not raw.lstrip()[:1] in (b"{", b"["):
                return None
            raw = raw.decode("utf-8", "ignore")
        if isinstance(raw, str) and raw.lstrip()[:1] in ("{", "["):
            return json.loads(raw)
    except Exception:  # noqa: BLE001
        return None
    return None


def _form_field(raw, name):
    """Very small multipart reader for `model=` in image edit / transcription uploads."""
    try:
        if isinstance(raw, (bytes, bytearray)):
            key = f'name="{name}"'.encode()
            i = raw.find(key)
            if i < 0:
                return None
            j = raw.find(b"\r\n\r\n", i)
            k = raw.find(b"\r\n", j + 4)
            return raw[j + 4:k].decode("utf-8", "ignore")[:80]
    except Exception:  # noqa: BLE001
        return None
    return None


def _add(**k):
    if len(_items) < _MAX:
        _items.append({x: y for x, y in k.items() if y not in (None, "", 0, 0.0)})


def record(host: str, path: str, status: int, req_body, resp_json, headers) -> None:
    if status >= 400:
        return
    host = (host or "").lower()
    path = path or ""
    if "anthropic.com" in host and "/messages" in path:
        u = (resp_json or {}).get("usage") or {}
        if u:
            _add(p="anthropic", k="text", m=(resp_json or {}).get("model"), i=u.get("input_tokens"), o=u.get("output_tokens"),
                 cw=u.get("cache_creation_input_tokens"), cr=u.get("cache_read_input_tokens"))
        return
    if "openai.com" in host:
        rq = _body_json(req_body) or {}
        model = rq.get("model") or _form_field(req_body, "model")
        u = (resp_json or {}).get("usage") or {}
        if "/images" in path:
            det = u.get("input_tokens_details") or {}
            n = len((resp_json or {}).get("data") or []) or int(_num(rq.get("n")) or 1)
            _add(p="openai", k="image", m=model or "image", n=n, i=det.get("text_tokens") or (u.get("input_tokens") if not det else None),
                 ii=det.get("image_tokens"), o=u.get("output_tokens"), size=rq.get("size"), q=rq.get("quality"))
        elif "/audio/speech" in path:
            _add(p="openai", k="audio", m=model or "tts", ch=len(str(rq.get("input") or "")))
        elif "/audio/transcriptions" in path or "/audio/translations" in path:
            _add(p="openai", k="stt", m=model or "whisper-1", sec=_num((resp_json or {}).get("duration")), n=1)
        elif u:
            _add(p="openai", k="text", m=(resp_json or {}).get("model") or model, i=u.get("prompt_tokens") or u.get("input_tokens"),
                 o=u.get("completion_tokens") or u.get("output_tokens"))
        return
    if "elevenlabs.io" in host:
        if ("/user" in path or "/models" in path or "/voices" in path) and "text-to" not in path:
            return
        cost = headers.get("character-cost") if headers else None
        rq = _body_json(req_body) or {}
        kind = "music" if "/music" in path else "stt" if "speech-to-text" in path else "sfx" if "sound-generation" in path else "audio"
        _add(p="elevenlabs", k=kind, m=rq.get("model_id") or kind, c=_num(cost) if cost else None,
             ch=len(str(rq.get("text") or "")) if kind == "audio" and not cost else None,
             ms=_num(rq.get("music_length_ms")) if kind == "music" else None, n=1)
        return
    if "klingai.com" in host:
        d = (resp_json or {}).get("data") or {}
        if isinstance(d, dict) and d.get("task_status") == "succeed":
            tid = d.get("task_id")
            if tid and tid in _seen_tasks:
                return
            _seen_tasks.add(tid)
            units = _num(d.get("final_unit_deduction"))
            kind = "image" if "/images" in path else "video"
            _add(p="kling", k=kind, m=kind, u=units, n=1)
        return


def _hdrs(h):
    try:
        return {k.lower(): v for k, v in dict(h).items() if k.lower() in ("character-cost",)}
    except Exception:  # noqa: BLE001
        return {}


def _patch_requests():
    try:
        import requests  # noqa: F401
        from requests.sessions import Session
    except Exception:  # noqa: BLE001
        return
    orig = Session.send
    if getattr(orig, "_jarvis", False):
        return

    def send(self, request, **kw):
        resp = orig(self, request, **kw)
        try:
            from urllib.parse import urlsplit
            u = urlsplit(request.url)
            if any(h in u.hostname or "" for h in ("anthropic.com", "openai.com", "elevenlabs.io", "klingai.com")):
                js = None
                if not kw.get("stream") and "json" in (resp.headers.get("content-type") or ""):
                    js = resp.json()
                record(u.hostname, u.path, resp.status_code, request.body, js, _hdrs(resp.headers))
        except Exception:  # noqa: BLE001
            pass
        return resp
    send._jarvis = True
    Session.send = send


def _patch_httpx():
    try:
        import httpx
    except Exception:  # noqa: BLE001
        return

    def wrap(cls, is_async):
        orig = cls.send
        if getattr(orig, "_jarvis", False):
            return

        def look(request, resp):
            try:
                host = request.url.host or ""
                if any(h in host for h in ("anthropic.com", "openai.com", "elevenlabs.io", "klingai.com")):
                    js = None
                    if hasattr(resp, "_content") and "json" in (resp.headers.get("content-type") or ""):
                        js = json.loads(resp._content)
                    body = request.content if hasattr(request, "_content") else None
                    record(host, request.url.path, resp.status_code, body, js, _hdrs(resp.headers))
            except Exception:  # noqa: BLE001
                pass

        if is_async:
            async def send(self, request, **kw):
                resp = await orig(self, request, **kw)
                look(request, resp)
                return resp
        else:
            def send(self, request, **kw):
                resp = orig(self, request, **kw)
                look(request, resp)
                return resp
        send._jarvis = True
        cls.send = send

    wrap(httpx.Client, False)
    wrap(httpx.AsyncClient, True)


def _flush():
    if not _items:
        return
    try:
        line = "JARVIS_USAGE " + json.dumps({"v": 1, "items": _items}, separators=(",", ":"), ensure_ascii=True)
        sys.stdout.flush()
        print(line[:200_000], flush=True)
    except Exception:  # noqa: BLE001
        pass


if os.environ.get("JARVIS_USAGE_OFF") != "1":
    _patch_requests()
    _patch_httpx()
    atexit.register(_flush)
