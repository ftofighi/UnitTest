from fastapi import APIRouter

from controller.user import router as user_router


router = APIRouter()
router.include_router(user_router, prefix="/User")