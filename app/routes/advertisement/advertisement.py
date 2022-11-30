from fastapi import APIRouter, Depends
from starlette.responses import Response

from app.exceptions.exceptions import NotFoundError
from app.models.base_models.requests.advertisement import (
    GetAdvertisementsRequest,
    PatchAdvertisementRequest,
)
from app.models.base_models.responses.advertisement import GetAdvertisementsResponse
from app.services.advertisement_service import AdvertisementService
from db_setup import get_session, engine

advertisement_router = APIRouter(prefix="/advertisement")


@advertisement_router.get(
    "", description="광고 송출 요청", response_model=GetAdvertisementsResponse
)
@get_session(name="session")
async def get_advertisements(
    request: GetAdvertisementsRequest = Depends(), session=None
):
    advertisement_service = AdvertisementService()
    result = await advertisement_service.get_advertisements(
        user_id=request.user_id,
        country=request.country,
        gender=request.gender,
        session=session,
    )
    return GetAdvertisementsResponse(result=result)


@advertisement_router.patch("/{ad_campaign_id}", description="광고 리워드 수정")
@get_session(name="session")
async def patch_advertisement_reward(
    ad_campaign_id: int, request: PatchAdvertisementRequest, session=None
):
    reward = request.reward
    if reward < 0:
        return Response(status_code=400)
    # jwt token으로 관리자인지 인증을 하고 API호출을 해야하나, 과제설명에서 API인증에 대한 부분은 생각하지 않아도 된다고 하므로 그대로 진행함.
    try:
        advertisement_service = AdvertisementService()
        await advertisement_service.patch_advertisement_reward(
            ad_campaign_id=ad_campaign_id, reward=reward, session=session
        )
        return Response(status_code=200)
    except NotFoundError as e:
        return Response(status_code=404)
    except Exception as e:
        return Response(status_code=500)
