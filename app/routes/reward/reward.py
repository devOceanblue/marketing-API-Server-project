from fastapi import APIRouter
from starlette.responses import Response

from app.exceptions.exceptions import NotFoundError, NotEnoughBalanceError
from app.models.base_models.requests.reward import UserRewardRequest, EarnRewardRequest
from app.models.base_models.responses.reward import GetWeeklyRewardsResponse
from app.services.reward_sevice import RewardService
from db_setup import get_session
from fastapi.logger import logger

reward_router = APIRouter(prefix="/reward")


@reward_router.get("", description="리워드 내역 확인", response_model=GetWeeklyRewardsResponse)
@get_session(name="session")
async def get_weekly_rewards(session=None):
    reward_service = RewardService()

    try:
        result = await reward_service.get_weekly_rewards(session=session)
        return result
    except NotFoundError as e:
        logger.error(e)
        return Response(status_code=404)


@reward_router.get("/{user_id}", description="리워드 잔액 확인")
@get_session(name="session")
async def get_balance_of_rewards(user_id: int, session=None):
    reward_service = RewardService()
    try:
        result = await reward_service.get_balance_of_reward(
            user_id=user_id, session=session
        )
        return result
    except NotFoundError as e:
        logger.error(e)
        return Response(status_code=404)


@reward_router.patch("/use/{user_id}", description="리워드 차감")
@get_session(name="session")
async def use_reward(user_id: int, request: UserRewardRequest, session=None):
    reward_service = RewardService()
    try:
        result = await reward_service.use_reward(
            user_id=user_id, reward=request.reward, session=session
        )
        return result
    except NotEnoughBalanceError as e:
        logger.warning(e)
        return Response(status_code=400)


@reward_router.patch("/earn/{user_id}", description="리워드 적립")
@get_session(name="session")
async def earn_reward(user_id: int, request: EarnRewardRequest, session=None):
    reward_service = RewardService()
    try:
        result = await reward_service.earn_reward(
            user_id=user_id, reward=request.reward, session=session
        )
        return result
    except NotFoundError as e:
        logger.error(e)
        return Response(status_code=404)
