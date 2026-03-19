import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

VECTOR_DB_DIR = os.path.join(BASE_DIR, "vectordb")
FAISS_INDEX_PATH = os.path.join(VECTOR_DB_DIR, "index.faiss")
METADATA_PATH = os.path.join(VECTOR_DB_DIR, "metadata.pkl")

MODEL_NAME = "all-MiniLM-L6-v2"
HF_DATASET = "ImeshThana/interview_questions"