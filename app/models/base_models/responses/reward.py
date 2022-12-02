from typing import List

from pydantic import BaseModel


class WeeklyRewardResponse(BaseModel):
    user_id: int
    credit: int
    created_at: str


class GetWeeklyRewardsResponse(BaseModel):
    result: List[WeeklyRewardResponse]


class GetBalanceOfRewardResponse(BaseModel):
    user_id: int
    balance: int
