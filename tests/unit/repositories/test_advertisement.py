import pytest

from app.repositories.advertisement_repository import AdvertisementRepo
from db_setup import SessionLocal


@pytest.mark.asyncio
async def test_get_adrvertisement():
    session = SessionLocal()
    advertisement_repo = AdvertisementRepo()
    resp = advertisement_repo.get_advertisements(
        user_id=1, country="KR", gender="F", session=session
    )
    assert resp


@pytest.mark.asyncio
async def test_get_advertisement():
    session = SessionLocal()
    advertisement_repo = AdvertisementRepo()
    resp = advertisement_repo.get_advertisement(ad_campaign_id=1, session=session)
    assert resp


@pytest.mark.asyncio
async def test_patch_advertisement_reward():
    session = SessionLocal()
    advertisement_repo = AdvertisementRepo()
    resp = advertisement_repo.patch_advertisement_reward(
        ad_campaign_id=1, reward=1, session=session
    )
    assert resp
