from app.exceptions.exceptions import NotFoundError, NotEnoughBalanceError
from app.models.base_models.responses.reward import (
    WeeklyRewardResponse,
    GetWeeklyRewardsResponse,
    GetBalanceOfRewardResponse,
)
from app.repositories.advertisement_repository import AdvertisementRepo
from app.repositories.reward_repository import RewardRepo
from fastapi.logger import logger


class RewardService:
    def __init__(self):
        self.reward_repo = RewardRepo()

    async def get_weekly_rewards(self, session):
        rv = await self.reward_repo.get_weekly_rewards(session=session)
        if not rv:
            raise NotFoundError

        result = [
            WeeklyRewardResponse(
                user_id=r.user_id, credit=r.credit, created_at=str(r.created_at)
            )
            for r in rv
        ]
        return GetWeeklyRewardsResponse(result=result)

    async def get_balance_of_reward(self, user_id: int, session):
        rv = await self.reward_repo.get_balance_of_reward(
            user_id=user_id, session=session
        )
        return GetBalanceOfRewardResponse(user_id=rv.user_id, balance=rv.balance)

    async def use_reward(self, user_id: int, reward: int, session):
        rv = await self.reward_repo.use_reward(
            user_id=user_id, reward=reward, session=session
        )

    async def earn_reward(self, user_id: int, reward: int, session):
        rv = await self.reward_repo.earn_reward(
            user_id=user_id, reward=reward, session=session
        )
        return
