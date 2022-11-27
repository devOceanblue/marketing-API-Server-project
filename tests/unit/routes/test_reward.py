from pprint import pprint

import pytest


@pytest.mark.asyncio
async def test_get_weekly_rewards(client):
    resp = client.get("/reward")
    pprint(resp.json())
