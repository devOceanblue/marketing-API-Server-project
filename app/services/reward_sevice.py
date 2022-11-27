from app.exceptions.exceptions import NotFoundError
from app.models.base_models.responses.reward import (
    WeeklyRewardResponse,
    GetWeeklyRewardsResponse,
)
from app.repositories.reward_repository import RewardRepo


class RewardService:
    def __init__(self):
        self.advertisement_repo = RewardRepo()

    async def get_weekly_rewards(self, session):
        rv = await self.advertisement_repo.get_weekly_rewards(session=session)
        if not rv:
            raise NotFoundError

        result = [
            WeeklyRewardResponse(
                user_id=r.user_id, credit=r.credit, created_at=str(r.created_at)
            )
            for r in rv
        ]
        return GetWeeklyRewardsResponse(result=result)
