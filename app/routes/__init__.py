from fastapi import APIRouter

from app.routes.advertisement.advertisement import advertisement_router
from app.routes.reward.reward import reward_router

main_router = APIRouter(prefix="")

blueprints = [advertisement_router, reward_router]


for router in blueprints:
    main_router.include_router(router)
