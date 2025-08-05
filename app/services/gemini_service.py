
from app.config.gemini_client import model
from app.services import embedding_service
from app.config.supabase_client import supabase

def generate_text(prompt: str):
    # Create an embedding for the user's prompt
    embedding = embedding_service.create_embedding(prompt)

    # Query Supabase for similar documents
    similar_docs = supabase.rpc(
        "match_documents", {"query_embedding": embedding, "match_threshold": 0.78, "match_count": 5}
    ).execute()

    # Combine the prompt with the context from the documents
    context = "\n".join([doc["content"] for doc in similar_docs.data])
    prompt_with_context = f"""Context:
{context}

Question: {prompt}

Answer:"""

    # Generate a response using the Gemini model
    response = model.generate_content(prompt_with_context)

    return response.text
