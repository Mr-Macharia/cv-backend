
from app.models.chat_model import ChatRequest
from app.services import gemini_service

def handle_chat(chat_request: ChatRequest):
    response = gemini_service.generate_text(chat_request.message)
    return {"response": response}
