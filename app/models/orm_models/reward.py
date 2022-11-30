from sqlalchemy import Integer, Column, TIMESTAMP, FetchedValue, func, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Reward(Base):
    __tablename__ = "reward"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    ad_campaign_id = Column(Integer, ForeignKey("ad_campaigns.id"), nullable=False)
    credit = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=FetchedValue(),
        server_onupdate=FetchedValue(),
    )

    def __init__(self, user_id: int, ad_campaign_id: int, credit: int):
        self.user_id = user_id
        self.ad_campaign_id = ad_campaign_id
        self.credit = credit
