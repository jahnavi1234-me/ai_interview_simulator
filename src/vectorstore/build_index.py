import os
import faiss
import pickle
from src.utils.config import FAISS_INDEX_PATH, METADATA_PATH, MODEL_NAME, VECTOR_DB_DIR
from src.data_loader.loader import load_data
from src.embeddings.model import EmbeddingModel


def build_faiss_index():
    os.makedirs(VECTOR_DB_DIR, exist_ok=True)

    print("📥 Loading dataset...")
    df = load_data("ImeshThana/interview_questions")

    texts = df["question"].tolist()

    print("🔍 Generating embeddings...")
    embedder = EmbeddingModel(MODEL_NAME)
    embeddings = embedder.encode(texts)

    dim = embeddings.shape[1]

    print("⚡ Building FAISS index...")
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    print("💾 Saving index...")
    faiss.write_index(index, FAISS_INDEX_PATH)

    metadata = df.to_dict(orient="records")

    with open(METADATA_PATH, "wb") as f:
        pickle.dump(metadata, f)

    print("✅ FAISS index built successfully!")