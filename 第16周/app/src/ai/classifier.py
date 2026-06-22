def classify_question(question):
    if not question:
        return "general"
    q = question.lower().strip()

    minecraft_keywords = [
        "minecraft", "hypixel", "mod", "server", "plugin",
        "fabric", "forge", "paper", "spigot", "aternos"
    ]

    coding_keywords = [
        "python", "code", "bug", "error", "program", "function",
        "variable", "compile", "runtime"
    ]

    math_keywords = [
        "solve", "math", "equation", "calculate", "integral",
        "derivative", "factor", "simplify"
    ]

    if any(k in q for k in minecraft_keywords):
        return "minecraft"
    if any(k in q for k in coding_keywords):
        return "coding"
    if any(k in q for k in math_keywords):
        return "math"
    else:
        return "general"
