import re


def validate_input(text, min_len=3, max_len=2000):
    if not text or not text.strip():
        return False, "Input cannot be empty."

    s = text.strip()
    if len(s) < min_len:
        return False, f"Input too short (min {min_len} chars)."

    if len(s) > max_len:
        return False, f"Input too long (max {max_len} chars)."

    # disallow common script tags or binary data
    if re.search(r"<\s*script|<\?|\?>|\bDROP\s+TABLE\b", s, re.IGNORECASE):
        return False, "Input contains disallowed patterns."

    # detect very long repeated characters which may be an attack
    if re.search(r"(.)\1{50,}", s):
        return False, "Input contains suspicious repeated characters."

    # basic ratio check: too many non-printable or non-word chars
    non_word = re.findall(r"[^\w\s.,;:'\"()\[\]{}!?+-]", s)
    if len(non_word) / max(1, len(s)) > 0.3:
        return False, "Input contains excessive special characters."

    return True, ""
