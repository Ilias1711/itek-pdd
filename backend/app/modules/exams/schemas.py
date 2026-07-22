from pydantic import BaseModel, Field


class ExamCreate(BaseModel):
    category_id: int = Field(gt=0)
    question_count: int = Field(gt=0)
    duration_minutes: int = Field(gt=0)
    allowed_mistakes: int = Field(ge=0)