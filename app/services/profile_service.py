from app.config.supabase_client import supabase
from app.models.user_model import UserProfile

def get_profile():
    response = supabase.table("profiles").select("*").eq("id", 1).single().execute()
    if response.data:
        return UserProfile(**response.data)
    return UserProfile()

def update_profile(profile_data: UserProfile):
    profile_dict = profile_data.model_dump(exclude_unset=True)
    if not profile_dict:
        return get_profile()

    response = supabase.table("profiles").update(profile_dict).eq("id", 1).execute()
    if response.data:
        return UserProfile(**response.data[0])
    return None
