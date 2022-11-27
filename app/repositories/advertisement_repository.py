from sqlalchemy import and_

from app.models.orm_models.advertisement import Advertisement


class AdvertisementRepo:
    async def get_advertisement(self, user_id: int, country: str, gender: str, session):
        qry = session.query(Advertisement).filter(
            and_(
                Advertisement.target_country == country,
                Advertisement.target_gender == gender,
            )
        )
        rv = session.execute(qry).scalars().fetchall()
        return rv
