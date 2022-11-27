from fastapi import APIRouter, Depends

from app.models.base_models.requests.advertisement import GetAdvertisementRequest
from app.models.base_models.responses.advertisement import GetAdvertisementResponse
from db_setup import get_session, engine

advertisement_router = APIRouter(prefix="/advertisement")


@advertisement_router.get(
    "",
    description="광고 리스트 불러오기",  # response_model=GetAdvertisementResponse
)
@get_session(name="session")
async def get_advertisement(request: GetAdvertisementRequest = Depends(), session=None):
    print()
    return "Success!"
