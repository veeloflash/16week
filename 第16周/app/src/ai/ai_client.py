import os
import requests
from requests.adapters import HTTPAdapter, Retry
from json import JSONDecodeError
from src.ai.prompt_builder import build_prompt
from src.security.input_validator import validate_input
from src.security.prompt_guard import check_prompt_injection

# Get API key from environment variable (secure practice)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not set in environment. Set GROQ_API_KEY before running.")

_session = requests.Session()
_retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
_session.mount("https://", HTTPAdapter(max_retries=_retries))


def ask_ai(question, timeout=10):
    ok, msg = validate_input(question)
    if not ok:
        return f"[Input Validation Error] {msg}"

    prompt = build_prompt(question)

    guard_ok, guard_msg = check_prompt_injection(prompt)
    if not guard_ok:
        return f"[Prompt Guard] {guard_msg}"

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        resp = _session.post(url, json=payload, headers=headers, timeout=timeout)
        resp.raise_for_status()
    except requests.RequestException as e:
        return f"[Network/Error] {str(e)}"

    try:
        data = resp.json()
    except JSONDecodeError as e:
        return f"[Response Parse Error] {str(e)}"

    try:
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[Response Format Error] {str(e)}"
