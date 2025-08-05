from app.services import profile_service, gemini_service
from app.models.document_model import CVRequest

def build_cv(cv_request: CVRequest):
    # 1. Get user profile
    user_profile = profile_service.get_profile()

    # 2. Create a detailed prompt for the Gemini model
    prompt = f"""
    Generate a professional CV for {user_profile.full_name} for the position of {cv_request.job_title}.
    The CV should be tailored to the following job description:
    ---
    {cv_request.job_description}
    ---

    Here is the user's professional information:
    - Full Name: {user_profile.full_name}
    - Email: {user_profile.email}
    - Phone Number: {user_profile.phone_number}
    - Address: {user_profile.address}
    - LinkedIn: {user_profile.linkedin_url}
    - GitHub: {user_profile.github_url}

    Personal Profile:
    {user_profile.personal_profile}

    Work Experience:
    {"".join([f"- {exp.job_title} at {exp.company} ({exp.start_date} - {exp.end_date})\\n  Responsibilities: {', '.join(exp.responsibilities)}\\n" for exp in user_profile.work_experience])}

    Education:
    {"".join([f"- {edu.degree} from {edu.institution} ({edu.start_date} - {edu.end_date})\\n" for edu in user_profile.education])}

    Skills:
    {", ".join(user_profile.skills)}

    Please generate a CV in British English that is well-structured, professional, and highlights the user's most relevant skills and experience for the job.
    The output should be a single string containing the full CV.
    """

    # 3. Generate the CV using the Gemini service
    # I am using the gemini_service but I will not use the RAG implementation for this
    # I will call the model directly
    from app.config.gemini_client import model
    response = model.generate_content(prompt)
    cv_content = response.text


    # 4. Return the generated CV
    return cv_content
