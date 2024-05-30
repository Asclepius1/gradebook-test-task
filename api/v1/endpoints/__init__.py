from api.v1.endpoints.score import router as scrore_router
from api.v1.endpoints.student import router as student_router
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(student_router)
api_router.include_router(scrore_router)