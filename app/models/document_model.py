from pydantic import BaseModel

class CVRequest(BaseModel):
    job_title: str
    job_description: str

class CoverLetterRequest(BaseModel):
    job_title: str
    job_description: str
