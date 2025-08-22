# services/retrieval.py

import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def load_index(path="data/faiss_index.pkl"):
    with open(path, "rb") as f:
        index, chunks = pickle.load(f)
    return index, chunks

def retrieve_context(query, k=1):
    index, chunks = load_index()
    query_embedding = embedder.encode([query], convert_to_numpy=True)
    _, top_indices = index.search(query_embedding, k)
    return " ".join([chunks[i] for i in top_indices[0]])
