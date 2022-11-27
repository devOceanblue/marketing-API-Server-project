from pydantic import BaseModel


class GetAdvertisementResponse(BaseModel):
    ad_campaign_id: int
    image_url: str
    landing_url: str
    reward: int