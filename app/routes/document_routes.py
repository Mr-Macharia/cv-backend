
from fastapi import APIRouter

router = APIRouter()

@router.post("/generate-cv")
def generate_cv():
    return {"message": "This is the generate CV endpoint"}

@router.post("/generate-cover-letter")
def generate_cover_letter():
    return {"message": "This is the generate cover letter endpoint"}
