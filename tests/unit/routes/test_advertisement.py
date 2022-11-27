import pytest


@pytest.mark.asyncio
async def test_get_advertisement(client):
    resp = client.get("/advertisement?user_id=1&gender=M&country=KR")
    print(resp.json())


def test_patch_advertisement_reward(client):
    resp = client.patch("/advertisement/1", json={"reward": 1111})
    print(resp)
