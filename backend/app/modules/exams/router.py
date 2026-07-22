from fastapi import APIRouter

from app.modules.exams.schemas import ExamCreate
from app.modules.exams.service import create_exam

router = APIRouter(
    prefix="/exams",
    tags=["exams"],
)


@router.post("")
async def create_exam_endpoint(exam_data: ExamCreate):
    return create_exam(exam_data)