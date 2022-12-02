from pydantic import ValidationError
import pytest

from app.exceptions.exceptions import NotEnoughBalanceError
from app.models.orm_models.reward import Reward
from app.models.orm_models.user import User
from app.repositories.reward_repository import RewardRepo
from app.services.reward_sevice import RewardService
from db_setup import SessionLocal


async def get_mock_user(*args, **kwargs):
    return User(user_id=1, country="KR", gender="M", balance=0)


async def get_mock_rewards(*args, **kwargs):
    return [Reward(user_id=1, ad_campaign_id=1, credit=300)]


async def mock_use_reward(*args, **waags):
    return


@pytest.mark.asyncio
async def test_get_weekly_rewards(monkeypatch):
    monkeypatch.setattr(RewardRepo, "get_weekly_rewards", get_mock_rewards)
    reward_service = RewardService()
    resp = await reward_service.get_weekly_rewards(session=None)
    assert resp


@pytest.mark.asyncio
async def test_get_balance_of_reward(monkeypatch):
    monkeypatch.setattr(RewardRepo, "get_balance_of_reward", get_mock_user)

    reward_service = RewardService()
    resp = await reward_service.get_balance_of_reward(user_id=1, session=None)
    assert all([resp.user_id == 1, resp.balance == 0])


@pytest.mark.asyncio
async def test_use_reward(monkeypatch):
    monkeypatch.setattr(RewardRepo, "use_reward", mock_use_reward)
    reward_service = RewardService()

    with pytest.raises(NotEnoughBalanceError):
        session = SessionLocal()
        await reward_service.use_reward(user_id=1, reward=float("inf"), session=session)
