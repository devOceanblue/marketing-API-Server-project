from fastapi import APIRouter

from app.routes.advertisement.advertisement import advertisement_router

router = APIRouter(prefix="/advertisement")

router.include_router(advertisement_router)


