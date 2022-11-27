from pydantic import BaseModel


class GetAdvertisementRequest(BaseModel):
    user_id: int
    gender: str
    country: str