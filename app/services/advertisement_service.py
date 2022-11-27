from app.models.base_models.responses.advertisement import (
    GetAdvertisementsResponse,
    AdvertisementResponseModel,
)
from app.repositories.advertisement_repository import AdvertisementRepo


class AdvertisementService:
    def __init__(self):
        self.advertisement_repo = AdvertisementRepo()

    async def get_advertisement(self, user_id: int, country: str, gender: str, session):
        advertisements = await self.advertisement_repo.get_advertisement(
            user_id=user_id, country=country, gender=gender, session=session
        )

        result = [
            AdvertisementResponseModel(
                ad_campaign_id=ad.id,
                image_url=ad.image_url,
                landing_url=ad.landing_url,
                reward=ad.reward,
            )
            for ad in advertisements
        ]

        return result
