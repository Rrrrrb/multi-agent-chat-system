from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class VectorStore:
    def __init__(self):
        self.texts = []
        self.metadata = []
        self.vectorizer = TfidfVectorizer()

    def add(self, text, meta):
        self.texts.append(text)
        self.metadata.append(meta)

    def search(self, query):
        if not self.texts:
            return None

        vectors = self.vectorizer.fit_transform(self.texts + [query])
        similarities = cosine_similarity(vectors[-1], vectors[:-1]) # type: ignore
        index = similarities.argmax()

        return self.metadata[index]
