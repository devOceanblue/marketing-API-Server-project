import random

import pytest


class TestEarnReward:
    @pytest.mark.asyncio
    async def test_earn_reward(self, client):
        data = {"ad_campaign_id": 1}
        resp = client.patch(f"/reward/earn/1", json=data)
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_earn_reward_fail_if_already_earned(self, client):
        data = {"ad_campaign_id": 1}
        resp = client.patch(f"/reward/earn/1", json=data)
        assert resp.status_code == 200

        data = {"ad_campaign_id": 1}
        resp = client.patch(f"/reward/earn/1", json=data)
        assert resp.status_code == 404


class TestGetWeeklyRewards:
    @pytest.mark.asyncio
    async def test_get_weekly_rewards(self, client):
        client.get("/advertisement?user_id=4&gender=M&country=KR")
        resp = client.get("/reward")
        assert resp.status_code == 200


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
