import json
import os
from datetime import datetime

# Write newline-delimited JSON (JSONL) per course requirements
LOG_DIR = "data"
LOG_FILE = os.path.join(LOG_DIR, "user_logs.jsonl")


def log_interaction(question, answer, category):
    os.makedirs(LOG_DIR, exist_ok=True)
    entry = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": answer,
        "category": category,
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
