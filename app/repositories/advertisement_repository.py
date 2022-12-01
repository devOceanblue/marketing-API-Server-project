from sqlalchemy import and_, update

from app.models.orm_models.advertisement import Advertisement


class AdvertisementRepo:
    async def get_advertisements(
        self, user_id: int, country: str, gender: str, session
    ):
        qry = session.query(Advertisement).filter(
            and_(
                Advertisement.target_country == country,
                Advertisement.target_gender == gender,
            )
        )
        rv = session.execute(qry).scalars().fetchall()
        return rv

    async def get_advertisement(self, ad_campaign_id: int, session):
        return session.query(Advertisement).get(ad_campaign_id)

    async def patch_advertisement_reward(
        self, ad_campaign_id: int, reward: int, session
    ):
        stmt = (
            update(Advertisement)
            .where(Advertisement.id == ad_campaign_id)
            .values(reward=reward)
        )
        session.execute(stmt)
