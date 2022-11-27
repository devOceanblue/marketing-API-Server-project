import pytest


@pytest.mark.asyncio
async def test_get_advertisement(client):
    resp = client.get("/advertisement")
    print(resp)


def test_one():
    assert 1 == 1
