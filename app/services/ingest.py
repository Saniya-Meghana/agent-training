from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader
import faiss
import numpy as np
import os
import pickle

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def load_pdf_chunks(pdf_path, chunk_size=300):
    reader = PdfReader(pdf_path)
    text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def save_index(index, chunks, path="data/faiss_index.pkl"):
    with open(path, "wb") as f:
        pickle.dump((index, chunks), f)

def build_index_from_pdf(pdf_path, persist=True):
    chunks = load_pdf_chunks(pdf_path)
    embeddings = embedder.encode(chunks, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    if persist:
        os.makedirs("data", exist_ok=True)
        save_index(index, chunks)

    return index, chunks
