# app/utils/prompt_builder.py

def build_prompt(query: str, context_chunks: list[str]) -> str:
    """Constructs a prompt for the LLM using the query and retrieved context."""
    context = '\n\n'.join(context_chunks)
    return f"Answer the following question using the provided context.\n\nContext:\n{context}\n\nQuestion: {query}"
