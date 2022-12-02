import pytest

from app.repositories.reward_repository import RewardRepo
from db_setup import SessionLocal


@pytest.mark.asyncio
async def test_get_weekly_rewards():
    session = SessionLocal()
    reward_repo = RewardRepo()
    resp = await reward_repo.get_weekly_rewards(session=session)


@pytest.mark.asyncio
async def test_get_balance_of_reward():
    session = SessionLocal()
    reward_repo = RewardRepo()
    resp = await reward_repo.get_balance_of_reward(user_id=1, session=session)


@pytest.mark.asyncio
async def test_earn_reward():
    session = SessionLocal()
    reward_repo = RewardRepo()

    resp = await reward_repo.get_balance_of_reward(user_id=1, session=session)
    balance_before = resp.balance
    credit = 1
    resp = await reward_repo.earn_reward(
        user_id=1, ad_campaign_id=1, credit=credit, session=session
    )
    resp = await reward_repo.get_balance_of_reward(user_id=1, session=session)
    balance_after = resp.balance
    assert balance_after - balance_before == credit


@pytest.mark.asyncio
async def test_use_reward():
    session = SessionLocal()
    reward_repo = RewardRepo()

    resp = await reward_repo.get_balance_of_reward(user_id=1, session=session)
    balance_before = resp.balance
    credit = 1
    resp = await reward_repo.use_reward(user_id=1, reward=credit, session=session)
    resp = await reward_repo.get_balance_of_reward(user_id=1, session=session)
    balance_after = resp.balance
    assert balance_before - balance_after == credit


@pytest.mark.asyncio
async def test_get_reward():
    session = SessionLocal()
    reward_repo = RewardRepo()
    resp = await reward_repo.get_reward(ad_campaign_id=1, user_id=1, session=session)
    assert resp
