import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self, embedding_model="all-MiniLM-L6-v2"):
        self.embedder = SentenceTransformer(embedding_model)
        self.index = None
        self.documents = []

    def build_index(self, docs):
        self.documents = docs
        embeddings = self.embedder.encode(docs, convert_to_numpy=True)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def retrieve(self, query, k=1):
        if self.index is None:
            raise ValueError("Index not built. Call build_index() first.")
        query_embedding = self.embedder.encode([query], convert_to_numpy=True)
        _, top_indices = self.index.search(query_embedding, k)
        return [self.documents[i] for i in top_indices[0]]
