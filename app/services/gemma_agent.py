from transformers import pipeline
import os
from dotenv import load_dotenv
from app.services.retrieval import retrieve_context 

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

generator = pipeline("text-generation", model="google/gemma-7b", token=HF_TOKEN)

def clean_response(text: str) -> str:
    text = text.strip()
    if text.endswith(",") or text.endswith(":"):
        text += "..."
    return text

def add_source(text: str, source: str = "GDPR Article 5") -> str:
    return f"{text}\n\n(Source: {source})"

def generate_response(query: str) -> str:
    context = retrieve_context(query) 
    prompt = f"{context}\n\nQuestion: {query}\nAnswer:"
    result = generator(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
    raw_text = result[0]["generated_text"]
    cleaned = clean_response(raw_text)
    final = add_source(cleaned)
    return final
