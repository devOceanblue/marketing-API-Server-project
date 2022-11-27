from datetime import datetime, timedelta

from app.models.orm_models.reward import Reward


class RewardRepo:
    async def get_weekly_rewards(self, session):
        qry = session.query(Reward).filter(
            Reward.created_at >= datetime.utcnow() - timedelta(days=7)
        )
        rv = session.execute(qry).scalars().fetchall()
        return rv
