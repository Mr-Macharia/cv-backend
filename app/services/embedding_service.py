
from app.config.gemini_client import model

def create_embedding(text):
    result = model.embed_content([text])
    return result['embedding']
