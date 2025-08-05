from app.services import profile_service
from app.models.user_model import UserProfile

def get_user_profile():
    return profile_service.get_profile()

def update_user_profile(profile_data: UserProfile):
    return profile_service.update_profile(profile_data)
