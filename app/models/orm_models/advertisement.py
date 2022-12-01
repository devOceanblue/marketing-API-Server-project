from sqlalchemy import Column, Integer, String, TIMESTAMP, func, FetchedValue, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Advertisement(Base):

    __tablename__ = "ad_campaigns"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    image_url = Column(String)
    landing_url = Column(String)
    weight = Column(Integer)
    target_country = Column(String)
    target_gender = Column(String)
    reward = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=FetchedValue(),
        server_onupdate=FetchedValue(),
    )

    def __init__(
        self,
        name,
        image_url,
        landing_url,
        weight,
        target_country,
        target_gender,
        reward,
    ):
        self.name = name
        self.image_url = image_url
        self.landing_url = landing_url
        self.weight = weight
        self.target_country = target_country
        self.target_gender = target_gender
        self.reward = reward
