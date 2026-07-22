from fastapi import FastAPI

from app.modules.exams.router import router as exams_router


app = FastAPI(
    title="ITEK Exam API",
    version="0.1.0",
)

app.include_router(exams_router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "itek-exam-api",
    }