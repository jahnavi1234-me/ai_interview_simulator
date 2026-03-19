import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import random
from src.rag.retriever import Retriever
from src.evaluator.evaluator import AnswerEvaluator

st.set_page_config(page_title="AI Interview Simulator")
st.title("🤖 AI Interview Simulator")

# -------- INIT --------
if "retriever" not in st.session_state:
    st.session_state.retriever = Retriever()

if "evaluator" not in st.session_state:
    st.session_state.evaluator = AnswerEvaluator()

# -------- STATE --------
if "started" not in st.session_state:
    st.session_state.started = False
if "results" not in st.session_state:
    st.session_state.results = []
if "submitted" not in st.session_state:
    st.session_state.submitted = {}
if "total_q" not in st.session_state:
    st.session_state.total_q = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# -------- START SCREEN --------
if not st.session_state.started:
    topic = st.text_input("Enter Topic")
    difficulty = st.selectbox("Select Difficulty", ["easy", "medium", "hard"])

    if st.button("Start Interview"):
        if topic:
            questions = st.session_state.retriever.retrieve(topic, difficulty=difficulty, top_k=100)
            unique_questions = list({q["question"]: q for q in questions}.values())
            random.shuffle(unique_questions)

            if len(unique_questions) == 0:
                st.error("No questions found. Try another topic.")
                st.stop()

            st.session_state.questions = unique_questions[:10]
            st.session_state.total_q = len(st.session_state.questions)
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.started = True
            st.rerun()
        else:
            st.warning("Enter topic")

# -------- INTERVIEW --------
if st.session_state.started:
    questions = st.session_state.questions
    q_index = st.session_state.q_index
    total_q = st.session_state.total_q

    if q_index < total_q:
        q_data = questions[q_index]
        st.subheader(f"Question {q_index+1} / {total_q}")
        st.write(q_data["question"])
        answer = st.text_area("Your Answer", key=f"ans_{q_index}")

        col1, col2, col3 = st.columns(3)

        # SUBMIT
        with col1:
            if st.button("Submit Answer", key=f"submit_{q_index}"):
                score, _ = st.session_state.evaluator.evaluate(answer, q_data["answer"])
                st.session_state.results.append({
                    "question": q_data["question"],
                    "user_answer": answer,
                    "correct_answer": q_data["answer"],
                    "score": score
                })
                st.session_state.score += score
                st.session_state.submitted[q_index] = True

                st.success(f"Score: {round(score,2)}/100")
                st.write("✅ Correct Answer:", q_data["answer"])

        # NEXT
        with col2:
            if st.button("Next Question", key=f"next_{q_index}"):
                if q_index in st.session_state.submitted:
                    st.session_state.q_index += 1
                    st.rerun()
                else:
                    st.warning("Submit or skip first")

        # SKIP
        with col3:
            if st.button("Skip Question", key=f"skip_{q_index}"):
                st.session_state.results.append({
                    "question": q_data["question"],
                    "user_answer": "Skipped",
                    "correct_answer": q_data["answer"],
                    "score": 0
                })
                st.session_state.q_index += 1
                st.rerun()

        # END
        if st.button("End Interview"):
            st.session_state.q_index = total_q
            st.rerun()

    # FINAL RESULTS
    else:
        st.success("🎉 Interview Completed!")

        total = len(st.session_state.results)
        final_score = st.session_state.score / max(total, 1)
        st.write(f"### 🏆 Final Score: {round(final_score,2)}/100")

        # Strengths / Weaknesses / Improvements
        strengths, weaknesses, improvements = [], [], []
        for r in st.session_state.results:
            score = r["score"]
            if score >= 70:
                strengths.append(r["question"])
            elif score <= 40:
                weaknesses.append(r["question"])
                improvements.append(f"Review: {r['question']}")

        st.write(f"**Strengths:** {', '.join(strengths) if strengths else 'None'}")
        st.write(f"**Weaknesses:** {', '.join(weaknesses) if weaknesses else 'None'}")
        st.write(f"**Improvements:** {', '.join(improvements) if improvements else 'None'}")

        # RESTART SAFE
        if st.button("Restart"):
            st.session_state.clear()
            st.session_state.retriever = Retriever()
            st.session_state.evaluator = AnswerEvaluator()
            st.session_state.started = False
            st.session_state.results = []
            st.session_state.submitted = {}
            st.session_state.total_q = 0
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.rerun()