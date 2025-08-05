
from app.config.gemini_client import model
from app.services import data_extraction_service
from app.config.supabase_client import supabase
import json

def chat_with_user(user_message: str, session_id: str = "default_session"):
    # 1. Get chat history
    chat_history = supabase.table("chat_history").select("*").eq("session_id", session_id).order("created_at").execute()

    # 2. Create the prompt
    system_prompt = """
    You are a friendly and professional career assistant for Maryanne Njenga. Your goal is to gather her professional information through conversation.
    When you extract information, respond with a JSON object with the key "extracted_data" and a confirmation message.
    The JSON object should have a "type" field (e.g., "work_experience", "education", "skill") and a "data" field with the extracted information.
    Example:
    {
        "extracted_data": {
            "type": "work_experience",
            "data": {
                "job_title": "Software Engineer",
                "company": "Google",
                "start_date": "2022-01-01",
                "end_date": "2023-01-01",
                "responsibilities": ["Developed new features", "Fixed bugs"]
            }
        },
        "response": "Thanks! I've added your work experience at Google to your profile."
    }
    If you are not extracting data, just respond with a friendly message.
    """

    # The gemini api expects a list of dicts, let's build it
    messages = []
    for row in chat_history.data:
        messages.append({"role": "user", "parts": [{"text": row['user_message']}]})
        messages.append({"role": "model", "parts": [{"text": row['ai_message']}]})

    messages.append({"role": "user", "parts": [{"text": user_message}]})

    # 3. Generate a response
    chat = model.start_chat(history=messages)
    response = chat.send_message(system_prompt + "\n" + user_message)
    ai_response_text = response.text

    # 4. Parse the response and extract data
    try:
        response_json = json.loads(ai_response_text)
        if "extracted_data" in response_json:
            extracted_data = response_json["extracted_data"]
            data_type = extracted_data.get("type")
            data = extracted_data.get("data")
            if data_type == "work_experience":
                data_extraction_service.add_work_experience(data)
            elif data_type == "education":
                data_extraction_service.add_education(data)
            elif data_type == "skill":
                data_extraction_service.add_skill(data)
            ai_message_to_user = response_json.get("response", "I've updated your profile.")
        else:
            ai_message_to_user = ai_response_text

    except json.JSONDecodeError:
        ai_message_to_user = ai_response_text

    # 5. Save to chat history
    supabase.table("chat_history").insert({
        "session_id": session_id,
        "user_message": user_message,
        "ai_message": ai_message_to_user
    }).execute()

    return ai_message_to_user
