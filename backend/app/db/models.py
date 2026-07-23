from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.database import Base


class Exam(Base):
    __tablename__ = "exams"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    category_id: Mapped[int] = mapped_column(Integer)

    question_count: Mapped[int] = mapped_column(Integer)

    duration_minutes: Mapped[int] = mapped_column(Integer)

    allowed_mistakes: Mapped[int] = mapped_column(Integer)