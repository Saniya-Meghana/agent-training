def build_prompt(query: str, context_chunks: list[str]) -> str:
    """Constructs a prompt for the LLM using the query and retrieved context."""
    context = '

'.join(context_chunks)
    return f"Answer the following question using the provided context.

Context:
{context}

Question: {query}"
