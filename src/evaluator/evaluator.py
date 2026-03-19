from sklearn.metrics.pairwise import cosine_similarity
from src.embeddings.model import EmbeddingModel
from src.utils.config import MODEL_NAME


class AnswerEvaluator:
    def __init__(self):
        self.embedder = EmbeddingModel(MODEL_NAME)

    def evaluate(self, user_answer, correct_answer):
        vec1 = self.embedder.encode([user_answer])
        vec2 = self.embedder.encode([correct_answer])

        score = cosine_similarity(vec1, vec2)[0][0]

        score_percent = round(score * 100, 2)

        if score_percent > 80:
            feedback = "Excellent answer!"
        elif score_percent > 50:
            feedback = "Good, but can improve."
        else:
            feedback = "Needs improvement."

        return score_percent, feedback