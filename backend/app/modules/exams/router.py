from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.modules.exams.schemas import ExamCreate
from app.modules.exams.service import create_exam


router = APIRouter(
    prefix="/exams",
    tags=["exams"],
)


@router.post("")
async def create_exam_endpoint(
    exam_data: ExamCreate,
    db: Session = Depends(get_db),
):
    return create_exam(exam_data, db)