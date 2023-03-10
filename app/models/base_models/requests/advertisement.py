from pydantic import BaseModel


class GetAdvertisementsRequest(BaseModel):
    user_id: int
    gender: str
    country: str


class PatchAdvertisementRequest(BaseModel):
    reward: int
