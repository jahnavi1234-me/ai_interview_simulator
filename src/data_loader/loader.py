from datasets import load_dataset
import pandas as pd
import ast


def assign_difficulty(question):
    length = len(question)

    if length < 60:
        return "easy"
    elif length < 120:
        return "medium"
    else:
        return "hard"


def load_data(dataset_name):
    dataset = load_dataset(dataset_name)

    data = dataset["train"]

    inputs = data["input"]
    qa_list = data["question_answer"]

    rows = []

    for topic, qa in zip(inputs, qa_list):

        # 🔥 FIX: convert string → dict
        if isinstance(qa, str):
            try:
                qa = ast.literal_eval(qa)
            except:
                continue

        if isinstance(qa, dict):
            question = qa.get("question", "")
            answer = qa.get("answer", "")

            if question and answer:
                difficulty = assign_difficulty(question)

                rows.append({
                    "topic": str(topic).lower().strip(),
                    "question": question,
                    "answer": answer,
                    "difficulty": difficulty
                })

    df = pd.DataFrame(rows)

    print(f"✅ Loaded {len(df)} questions")

    return df