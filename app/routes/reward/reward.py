from fastapi import APIRouter

from app.models.base_models.requests.reward import UserRewardRequest, EarnRewardRequest
from db_setup import get_session

reward_router = APIRouter(prefix="/reward")


@reward_router.get("", description="리워드 내역 확인")
@get_session(name="session")
async def get_weekly_rewards(session=None):
    pass


@reward_router.get("/{user_id}", description="리워드 잔액 확인")
@get_session(name="session")
async def get_balance_of_reward(user_id: int, session=None):
    pass


@reward_router.patch("/{user_id}", description="리워드 차감")
@get_session(name="session")
async def use_reward(user_id: int, request: UserRewardRequest, session=None):
    pass


@reward_router.patch("/{user_id}", description="리워드 적립")
@get_session(name="session")
async def earn_reward(user_id: int, request: EarnRewardRequest, session=None):
    pass
