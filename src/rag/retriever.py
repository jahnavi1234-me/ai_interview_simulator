import faiss
import pickle
import os
from src.utils.config import FAISS_INDEX_PATH, METADATA_PATH, MODEL_NAME
from src.embeddings.model import EmbeddingModel

class Retriever:
    def __init__(self):
        if not os.path.exists(FAISS_INDEX_PATH):
            from src.vectorstore.build_index import build_faiss_index
            build_faiss_index()

        self.index = faiss.read_index(FAISS_INDEX_PATH)

        with open(METADATA_PATH, "rb") as f:
            self.metadata = pickle.load(f)

        self.embedder = EmbeddingModel(MODEL_NAME)

    def retrieve(self, query, difficulty=None, top_k=100):
        query_vec = self.embedder.encode([query])
        distances, indices = self.index.search(query_vec, top_k)

        results = []

        for idx in indices[0]:
            if idx == -1:
                continue
            item = self.metadata[idx]
            if difficulty:
                if item.get("difficulty", "easy") == difficulty:
                    results.append(item)
            else:
                results.append(item)

        # Remove duplicates
        unique = list({q["question"]: q for q in results}.values())

        # Ensure at least 10 questions
        if len(unique) < 10:
            for idx in indices[0]:
                if idx == -1:
                    continue
                item = self.metadata[idx]
                if item not in unique:
                    unique.append(item)
                if len(unique) >= 10:
                    break

        return unique[:10]