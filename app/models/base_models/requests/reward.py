from pydantic import BaseModel


class EarnRewardRequest(BaseModel):
    reward: int


class UserRewardRequest(BaseModel):
    reward: int
