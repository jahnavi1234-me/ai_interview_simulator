# AI Interview Simulator
## Project Description

The AI Interview Simulator is a Generative AI-based application that simulates real interview scenarios. It dynamically retrieves questions based on a given topic and difficulty level, evaluates user responses using semantic similarity, and provides structured feedback including strengths, weaknesses, and improvement suggestions.

This project helps users practice interviews, improve answering skills, and get AI-driven feedback.

## Problem Statement

Many students struggle with:

Lack of real interview practice

No personalized feedback on answers

Difficulty understanding strengths and weaknesses


This project solves these problems by providing:

AI-based interview simulation

Automated answer evaluation

Intelligent feedback generation

## Features

 Topic-based question retrieval

 Difficulty levels (Easy, Medium, Hard)

 Semantic similarity-based scoring

 Score out of 100 for each answer

 Displays correct answers

 Strengths & weaknesses analysis

 AI-generated final feedback

 Restart interview option

 FAISS-based fast retrieval system
## Technologies Used

Python 3.11

Streamlit – UI development

FAISS – Vector database

Sentence Transformers – Embeddings

Hugging Face Transformers – LLM feedback

Datasets Library – Interview dataset

NumPy – Numerical operations
## Project Architecture

User Input (Topic + Difficulty)
        ↓
Retriever (FAISS Vector Search)
        ↓
Top Questions Selected
        ↓
User Answers Input
        ↓
Evaluator (Semantic Similarity)
        ↓
Score Generation (0–100)
        ↓
LLM Feedback Generator
        ↓
Final Report (Score + Insights)


---

### Folder Structure

```
ai_interview_simulator/
│
├── app/
│   └── app.py
│
├── src/
│   ├── rag/
│   │   └── retriever.py
│   │
│   ├── embeddings/
│   │   └── model.py
│   │
│   ├── evaluator/
│   │   ├── evaluator.py
│   │   └── llm_feedback.py
│   │
│   ├── utils/
│   │   ├── config.py
│   │   └── vector_store.py
│
├── vectordb/
│
├── requirements.txt
│
└── README.md
```
## Installation & Setup

1️ Clone the repository

git clone https://github.com/your-username/ai_interview_simulator.git
cd ai_interview_simulator

2️ Create virtual environment

python -m venv venv

3️ Activate environment

Windows:


venv\Scripts\activate

4️ Install dependencies

pip install -r requirements.txt

5️ Run the application

streamlit run app/app.py
## Example Output

Question: What are decorators in Python?

Your Answer:Decorators in Python are functions that wrap another function to extend or modify its behavior without changing its original code.

Score: 92/100

Correct Answer:
Correct Answer: A decorator is a function that takes another function and extends its behavior without explicitly modifying it. It is a powerful tool for wrapping functions (e.g., for logging, timing, access control) using the @decorator_name syntax.

Final Score: 85/100

Strengths:
- Strong understanding of Python basics

Weaknesses:
- Needs improvement in advanced concepts

Improvements:
- Practice more coding-based questions

AI Feedback:
The candidate demonstrates good foundational knowledge...
<img width="1920" height="1080" alt="Screenshot (215)" src="https://github.com/user-attachments/assets/b2a85713-ee66-480a-969c-f4cc5927e192" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fa084005-2e2d-4b3b-9f6e-b986b858d207" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7a786f2d-d0dc-4a8d-86a7-dee21f599716" />

## Future Improvements

 Voice-based interview system

 Coding interview support

 Multi-language support

 Detailed analytics dashboard

 Cloud deployment (Docker + CI/CD)

 Advanced LLM integration (GPT / Llama)

## Author

Jahnavi Besabathini

