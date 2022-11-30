from pprint import pprint

import pytest


@pytest.mark.asyncio
async def test_get_weekly_rewards(client):
    resp = client.get("/reward")
    pprint(resp.json())


@pytest.mark.asyncio
async def test_get_balance_of_rewards(client):
    resp = client.get("/reward/1")
    pprint(resp.json())


@pytest.mark.asyncio
async def test_use_reward(client):
    data = {"reward": 1}
    resp = client.patch("/reward/use/1", json=data)
    pprint(resp.json())


@pytest.mark.asyncio
async def test_earn_reward(client):
    data = {"reward": 1}
    resp = client.patch("/reward/earn/1", json=data)
    pprint(resp.json())
