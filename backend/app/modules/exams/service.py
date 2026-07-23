from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.db.models import Exam
from app.modules.exams.schemas import ExamCreate


def create_exam(
    exam_data: ExamCreate,
    db: Session,
) -> dict:
    if exam_data.allowed_mistakes > exam_data.question_count:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Allowed mistakes cannot exceed question count",
        )

    exam = Exam(
        category_id=exam_data.category_id,
        question_count=exam_data.question_count,
        duration_minutes=exam_data.duration_minutes,
        allowed_mistakes=exam_data.allowed_mistakes,
    )

    db.add(exam)
    db.commit()
    db.refresh(exam)

    return {
        "message": "Exam created successfully",
        "exam": {
            "id": exam.id,
            "category_id": exam.category_id,
            "question_count": exam.question_count,
            "duration_minutes": exam.duration_minutes,
            "allowed_mistakes": exam.allowed_mistakes,
        },
    }