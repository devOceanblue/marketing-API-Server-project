from fastapi import APIRouter

from app.routes.reward.reward import reward_router

router = APIRouter(prefix="/reward")


router.include_router(reward_router)