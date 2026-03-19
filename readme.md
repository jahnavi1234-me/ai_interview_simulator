# AI Interview Simulator

## Overview

AI Interview Simulator is an intelligent system that simulates a real technical interview using Generative AI.  
The system dynamically retrieves interview questions based on topic and difficulty, evaluates candidate answers using an LLM, and generates a final performance report.

The project combines Retrieval Augmented Generation (RAG), vector search, and LLM evaluation to create an automated interview environment.

---

## Problem Statement

Technical interview preparation is difficult because:

- Candidates do not get realistic interview simulations
- Manual evaluation of answers is time consuming
- Practicing with static question lists does not reflect real interview scenarios
- Feedback is often unavailable or delayed

This project solves these problems by building an **AI powered interview simulator** that:

- retrieves relevant interview questions
- evaluates candidate answers automatically
- provides structured feedback and scoring
- generates a final interview performance report

---

## Key Features

- Topic based interview simulation
- Difficulty selection (Easy / Medium / Hard)
- Semantic question retrieval using vector search
- LLM based answer evaluation
- Skill extraction from candidate responses
- Automatic final interview report
- Streamlit based interactive interface
- Time tracking during interview

---

## System Architecture

User → Streamlit UI  
↓  
Interview Agent  
↓  
Question Retriever (RAG)  
↓  
Vector Database (FAISS)  
↓  
LLM Evaluation  
↓  
Interview Report Generator

---

## Technologies Used

- Python
- Streamlit
- FAISS Vector Database
- Sentence Transformers
- Ollama LLM (Mistral)
- Retrieval Augmented Generation (RAG)
- HuggingFace Datasets
- NumPy
- Regex based NLP

---

## Folder Structure
AI_Interview_Simulator

│
├── app
│ └── app.py
│
├── data
│ └── interviewQuestion.txt
│
├── src
│
│ ├── agent
│ │ └── interview_agent.py
│
│ ├── embeddings
│ │ └── embedding_model.py
│
│ ├── evaluator
│ │ ├── answer_evaluator.py
│ │ └── interview_report.py
│
│ ├── llm
│ │ └── llm_pipeline.py
│
│ ├── rag
│ │ └── question_retriever.py
│
│ ├── utils
│ │ ├── config.py
│ │ ├── skill_extractor.py
│ │ └── vectorStore.py
│
└── requirements.txt

---

## How It Works

1. Interview topic is entered by the user
2. Topic is converted into an embedding
3. FAISS vector database retrieves relevant questions
4. Questions are shown one by one to the user
5. User answers are evaluated by an LLM
6. Score and feedback are generated
7. Skills are extracted from responses
8. Final interview report is generated

---

## Dataset

Interview questions are loaded from:

HuggingFace Dataset:
`ImeshThana/interview_questions`

---

## Installation

```bash
pip install -r requirements.txt
Run Application
streamlit run app/app.py
## Future Improvements

Voice based interview

Multi-language interview support

Resume based personalized interviews

Real time emotion analysis

Interview analytics dashboard

## Author

Jahnavi
AI / Generative AI Projects