from fastapi import APIRouter, Depends

from app.models.base_models.requests.advertisement import GetAdvertisementsRequest
from app.models.base_models.responses.advertisement import GetAdvertisementsResponse
from app.services.advertisement_service import AdvertisementService
from db_setup import get_session, engine

advertisement_router = APIRouter(prefix="/advertisement")


@advertisement_router.get(
    "", description="광고 리스트 불러오기", response_model=GetAdvertisementsResponse
)
@get_session(name="session")
async def get_advertisement(
    request: GetAdvertisementsRequest = Depends(), session=None
):
    advertisement_service = AdvertisementService()
    result = await advertisement_service.get_advertisement(
        user_id=request.user_id,
        country=request.country,
        gender=request.gender,
        session=session,
    )
    return GetAdvertisementsResponse(result=result)
