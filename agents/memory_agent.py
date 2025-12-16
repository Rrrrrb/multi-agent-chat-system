from memory.vector_store import VectorStore

class MemoryAgent:
    def __init__(self):
        self.vector_store = VectorStore()
        self.history = []

    def store(self, record):
        print("[MemoryAgent] Storing information in memory")
        text = " ".join(record.get("results", [])) + " ".join(record.get("analysis", []))
        self.vector_store.add(text, record)
        self.history.append(record)

    def retrieve(self, query):
        print("[MemoryAgent] Retrieving from memory")
        return self.vector_store.search(query)
