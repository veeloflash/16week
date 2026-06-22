import pandas as pd

def load_logs():
    try:
        # Read newline-delimited JSON (JSONL) format with lines=True
        df = pd.read_json("data/user_logs.jsonl", lines=True)
        print(">>> df loaded, length =", len(df))
        return df
    except Exception as e:
        print(">>> JSON read error:", e)
        return pd.DataFrame()
