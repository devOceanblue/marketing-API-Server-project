from datetime import datetime, timedelta

from sqlalchemy import select, and_

from app.exceptions.exceptions import NotEnoughBalanceError
from app.models.orm_models.reward import Reward
from app.models.orm_models.user import User


class RewardRepo:
    async def get_weekly_rewards(self, session):
        qry = session.query(Reward).filter(
            Reward.created_at >= datetime.utcnow() - timedelta(days=7)
        )
        rv = session.execute(qry).scalars().fetchall()
        return rv

    async def get_balance_of_reward(self, user_id: int, session):
        return session.get(User, user_id)

    async def use_reward(self, user_id, reward: int, session):
        u = session.get(User, user_id)
        if u.balance - reward >= 0:
            u.balance -= reward
            session.commit()
        else:
            raise NotEnoughBalanceError

    async def earn_reward(self, user_id, ad_campaign_id: int, credit: int, session):
        u = session.get(User, user_id)
        u.balance += credit

        reward = Reward(user_id=user_id, ad_campaign_id=ad_campaign_id, credit=credit)
        session.add(reward)
        session.commit()

    async def get_reward(self, ad_campaign_id: int, user_id: int, session):
        stmt = select(Reward).where(
            and_(Reward.ad_campaign_id == ad_campaign_id, Reward.user_id == user_id)
        )
        rv = session.execute(stmt).all()
        return rv
