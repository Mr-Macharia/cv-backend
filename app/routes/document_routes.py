from fastapi import APIRouter
from app.controllers import document_controller
from app.models.document_model import CVRequest, CoverLetterRequest

router = APIRouter()

@router.post("/generate-cv")
def generate_cv(cv_request: CVRequest):
    return document_controller.handle_generate_cv(cv_request)

@router.post("/generate-cover-letter")
def generate_cover_letter(cover_letter_request: CoverLetterRequest):
    return document_controller.handle_generate_cover_letter(cover_letter_request)
