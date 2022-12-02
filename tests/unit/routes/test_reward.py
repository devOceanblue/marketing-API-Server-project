import random

import pytest
from sqlalchemy import delete

from app.models.orm_models.reward import Reward
from db_setup import SessionLocal


class TestEarnReward:
    @pytest.mark.asyncio
    async def test_earn_reward(self, client):
        data = {"ad_campaign_id": 2}
        resp = client.patch(f"/reward/earn/1", json=data)
        assert resp.status_code == 200

        session = SessionLocal()
        stmt = delete(Reward).where(Reward.user_id == 1)
        session.execute(stmt)
        session.commit()

    @pytest.mark.asyncio
    async def test_earn_reward_fail_if_already_earned(self, client):
        data = {"ad_campaign_id": 1}
        resp = client.patch(f"/reward/earn/1", json=data)
        assert resp.status_code == 200

        data = {"ad_campaign_id": 1}
        resp = client.patch(f"/reward/earn/1", json=data)
        assert resp.status_code == 404

        session = SessionLocal()
        stmt = delete(Reward).where(Reward.user_id == 1)
        session.execute(stmt)
        session.commit()


class TestGetWeeklyRewards:
    @pytest.mark.asyncio
    async def test_get_weekly_rewards(self, client):
        data = {"ad_campaign_id": 1}
        resp = client.patch(f"/reward/earn/4", json=data)
        assert resp.status_code == 200

        client.get("/advertisement?user_id=4&gender=M&country=KR")
        resp = client.get("/reward")
        assert resp.status_code == 200

        session = SessionLocal()
        stmt = delete(Reward).where(Reward.user_id == 4)
        session.execute(stmt)
        session.commit()


class TestGetBalanceOfRewards:
    @pytest.mark.asyncio
    async def test_get_balance_of_rewards(self, client):
        resp = client.get(f"/reward/1")
        assert resp.status_code == 200


class TestUseReward:
    @pytest.mark.asyncio
    async def test_use_reward(self, client):
        client.get("/advertisement?user_id=4&gender=M&country=KR")
        data = {"reward": 1}
        resp = client.patch(f"/reward/use/1", json=data)
        assert resp.status_code == 200
