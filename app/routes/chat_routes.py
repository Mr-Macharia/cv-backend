
from fastapi import APIRouter
from app.models.chat_model import ChatRequest
from app.controllers import chat_controller

router = APIRouter()

@router.post("/chat")
def chat_with_bot(chat_request: ChatRequest):
    return chat_controller.handle_chat(chat_request)
