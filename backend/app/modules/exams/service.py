from fastapi import HTTPException, status

from app.modules.exams.schemas import ExamCreate


def create_exam(exam_data: ExamCreate) -> dict:
    if exam_data.allowed_mistakes > exam_data.question_count:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Allowed mistakes cannot exceed question count",
        )

    return {
        "message": "Exam created successfully",
        "exam": exam_data.model_dump(),
    }