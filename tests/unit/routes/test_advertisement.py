import pytest


@pytest.mark.asyncio
async def test_get_advertisement(client):
    resp = client.get("/advertisement?user_id=1&gender=M&country=KR")
    print(resp.json())


def test_one():
    assert 1 == 1
