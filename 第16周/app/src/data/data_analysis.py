def analyze_logs(df):
    if df.empty:
        return {
            "total_questions": 0,
            "top_category": "None",
            "avg_answer_length": 0
        }

    total_questions = len(df)
    top_category = df["category"].value_counts().idxmax()
    avg_answer_length = df["answer"].apply(len).mean()

    return {
        "total_questions": total_questions,
        "top_category": top_category,
        "avg_answer_length": avg_answer_length
    }
