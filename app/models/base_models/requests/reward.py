from pydantic import BaseModel


class EarnRewardRequest(BaseModel):
    ad_campaign_id: int


class UserRewardRequest(BaseModel):
    reward: int
