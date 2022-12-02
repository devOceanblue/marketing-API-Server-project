import pytest
from pydantic import ValidationError

from app.models.orm_models.advertisement import Advertisement
from app.models.orm_models.user import User
from app.repositories.advertisement_repository import AdvertisementRepo
from app.repositories.user_repository import UserRepository
from app.services.advertisement_service import AdvertisementService


async def get_mock_user(*args, **kwargs):
    return User(user_id=1, country="KR", gender="M", balance=0)


async def get_mock_advertisements(*args, **kwargs):
    return [
        Advertisement(
            name="test",
            image_url="abc.jpg",
            landing_url="https://test",
            weight=300,
            target_country="KR",
            target_gender="M",
            reward=300,
        )
    ]


@pytest.mark.asyncio
async def test_get_advertisements(monkeypatch):

    monkeypatch.setattr(UserRepository, "get_user", get_mock_user)
    monkeypatch.setattr(
        AdvertisementRepo, "get_advertisements", get_mock_advertisements
    )

    with pytest.raises(ValidationError):
        advertisement_service = AdvertisementService()
        await advertisement_service.get_advertisements(
            user_id=1, country="KR", gender="M", session=None
        )
