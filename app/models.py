from datetime import date
from pydantic import BaseModel, Field, field_validator

class StudySessionCreate(BaseModel):
    subject: str = Field(min_length=1, max_length=80)
    study_hours: float = Field(ge=0, le=24)
    tasks_completed: int = Field(ge=0, le=1000)
    session_date: date

    @field_validator("subject")
    @classmethod
    def clean_subject(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Subject cannot be blank")
        return value

class StudySession(StudySessionCreate):
    id: int
