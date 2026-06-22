import re


INJECTION_PATTERNS = [
    r"ignore (previous|above) instructions",
    r"disregard (previous|above) instructions",
    r"don't follow previous",
    r"override the system prompt",
    r"insert this prompt",
    r"respond with.*only",
    r"give me the exact",
    # Additional security patterns for logic bypass attacks
    r"disregard the system prompt",
    r"reveal system prompt",
    r"reveal system prompts",
    r"include the admin password",
    r"admin password",
    r"secret key",
    r"api key",
    r"break the format",
    r"ignore safety mode",
    r"bypass security",
    r"jailbreak",
    r"ignore the instructions",
    r"pretend you are",
    r"roleplay as",
    r"act as.*without.*safety",
]


def check_prompt_injection(prompt):
    """Basic heuristic-based prompt injection detector.

    Returns (ok: bool, message: str).
    """
    if not prompt:
        return True, ""

    p = prompt.lower()
    for pat in INJECTION_PATTERNS:
        if re.search(pat, p):
            return False, "Detected potential prompt injection pattern."

    # suspicious control tokens
    if "<script" in p or "{{" in p or "}}" in p:
        return False, "Detected suspicious tokens in prompt."

    return True, ""
