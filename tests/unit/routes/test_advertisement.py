import pytest


class TestPatchAdvertisementReward:
    @pytest.mark.asyncio
    async def test_get_advertisement(self, client):
        resp = client.get("/advertisement?user_id=4&gender=M&country=KR")
        assert resp.status_code == 200

    @pytest.mark.asyncio
    def test_patch_advertisement_reward(self, client):
        resp = client.patch("/advertisement/1", json={"reward": 1111})
        assert resp.status_code == 200
