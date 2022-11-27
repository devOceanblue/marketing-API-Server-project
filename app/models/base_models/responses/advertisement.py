from typing import List

from pydantic import BaseModel


class AdvertisementResponseModel(BaseModel):
    ad_campaign_id: int
    image_url: str
    landing_url: str
    reward: int


class GetAdvertisementsResponse(BaseModel):
    result: List[AdvertisementResponseModel]
