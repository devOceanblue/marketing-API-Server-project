from datetime import datetime, timedelta

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

    async def earn_reward(self, user_id, reward: int, session):
        u = session.get(User, user_id)
        u.balance += reward
        session.commit()
