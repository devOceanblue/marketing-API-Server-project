import random
from random import random
from typing import List, Dict

import requests
import numpy as np

import config
from app.exceptions.exceptions import NotFoundError
from app.models.base_models.responses.advertisement import (
    GetAdvertisementsResponse,
    AdvertisementResponseModel,
)
from app.repositories.advertisement_repository import AdvertisementRepo
from app.repositories.user_repository import UserRepository


def _choose_advertisement(ads: List[Dict], type: int) -> List[Dict]:
    size = min(len(ads), 3)

    if type == 0:
        # random
        return random.shuffle(ads)[:size]
    elif type == 1:
        # weight, weight 기반의 정책에 대해 github에 제대로 적혀있지 않다. 관리자에게 한번더 물어보자.
        np.random.seed(np.random.randint(0, 100))
        weights = np.array([x["weight"] for x in ads])
        probability = weights / np.sum(weights)
        result = np.random.choice(ads, size=size, replace=False, p=probability)
        return result[:size]
    elif type == 2:
        # pctr
        return sorted(ads, key=lambda x: x["pctr"], reverse=True)[:size]
    else:
        # weight_pctr_mixed

        result = []
        pctr_sorted_ads = sorted(ads, key=lambda x: x["pctr"], reverse=True)
        result.append(pctr_sorted_ads[0])
        pctr_sorted_ads = pctr_sorted_ads[1:]
        if size > 1:
            np.random.seed(np.random.randint(0, 100))
            weights = np.array([x["weight"] for x in pctr_sorted_ads])
            probability = weights / np.sum(weights)
            result.extend(
                np.random.choice(
                    pctr_sorted_ads, size=size - 1, replace=False, p=probability
                )
            )
        return result


class AdvertisementService:
    def __init__(self):
        self.advertisement_repo = AdvertisementRepo()

    async def get_advertisements(
        self, user_id: int, country: str, gender: str, session
    ):
        user_repo = UserRepository()
        user = await user_repo.get_user(user_id=user_id, session=session)
        if not user:
            await user_repo.register_user(
                user_id=user_id, country=country, gender=gender, session=session
            )

        advertisements = await self.advertisement_repo.get_advertisements(
            user_id=user_id, country=country, gender=gender, session=session
        )
        if not advertisements:
            return advertisements

        pctr = (
            requests.get(
                f"{config.ctr_prediction_server}?user_id={user_id}&ad_campaign_ids={','.join([str(ad.id) for ad in advertisements])}"
            )
            .json()
            .get("pctr")
        )
        temp = [
            {
                "ad_campaign_id": ad.id,
                "image_url": ad.image_url,
                "landing_url": ad.landing_url,
                "reward": ad.reward,
                "weight": ad.weight,
                "pctr": p,
            }
            for ad, p in zip(advertisements, pctr)
        ]

        chosen_ads = _choose_advertisement(temp, user_id % 4)

        result = [
            AdvertisementResponseModel(
                ad_campaign_id=ad["ad_campaign_id"],
                image_url=ad["image_url"],
                landing_url=ad["landing_url"],
                reward=ad["reward"],
            )
            for ad in chosen_ads
        ]
        return result

    async def patch_advertisement_reward(
        self, ad_campaign_id: int, reward: int, session
    ):
        if rv := await self.advertisement_repo.get_advertisement(
            ad_campaign_id=ad_campaign_id, session=session
        ):
            await self.advertisement_repo.patch_advertisement_reward(
                ad_campaign_id=ad_campaign_id, reward=reward, session=session
            )
        else:
            raise NotFoundError
