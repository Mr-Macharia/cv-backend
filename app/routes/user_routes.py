from fastapi import APIRouter
from app.controllers import user_controller
from app.models.user_model import UserProfile

router = APIRouter()

@router.get("/profile", response_model=UserProfile)
def get_profile():
    return user_controller.get_user_profile()

@router.put("/profile", response_model=UserProfile)
def update_profile(profile_data: UserProfile):
    return user_controller.update_user_profile(profile_data)
