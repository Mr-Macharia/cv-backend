from app.models.chat_model import ChatRequest
from app.services import gemini_service

def handle_chat(chat_request: ChatRequest):
    # Assuming a single user, so a default session_id is fine
    response = gemini_service.chat_with_user(chat_request.message, session_id="maryanne_njenga")
    return {"response": response}
