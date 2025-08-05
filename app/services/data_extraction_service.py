from app.models.user_model import WorkExperience, Education
from app.services import profile_service

def add_work_experience(work_experience: WorkExperience):
    profile = profile_service.get_profile()
    profile.work_experience.append(work_experience)
    profile_service.update_profile(profile)

def add_education(education: Education):
    profile = profile_service.get_profile()
    profile.education.append(education)
    profile_service.update_profile(profile)

def add_skill(skill: str):
    profile = profile_service.get_profile()
    if skill not in profile.skills:
        profile.skills.append(skill)
        profile_service.update_profile(profile)

def update_personal_profile(personal_profile: str):
    profile = profile_service.get_profile()
    profile.personal_profile = personal_profile
    profile_service.update_profile(profile)
