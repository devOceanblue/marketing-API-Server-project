from fastapi import APIRouter

from app.routes.advertisement import advertisement_router
from app.routes.reward import reward_router

router = APIRouter(prefix="")

blueprints = [
    advertisement_router,
    reward_router
]



for router in blueprints:
    router.include_router(router)

