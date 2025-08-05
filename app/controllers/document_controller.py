from app.services import cv_builder, cover_letter_builder
from app.models.document_model import CVRequest, CoverLetterRequest

def handle_generate_cv(cv_request: CVRequest):
    return cv_builder.build_cv(cv_request)

def handle_generate_cover_letter(cover_letter_request: CoverLetterRequest):
    return cover_letter_builder.build_cover_letter(cover_letter_request)
