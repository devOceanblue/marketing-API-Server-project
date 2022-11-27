from sqlalchemy import Integer, Column, TIMESTAMP, FetchedValue, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Reward(Base):
    __tablename__ = "reward"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    credit = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=FetchedValue(),
        server_onupdate=FetchedValue(),
    )
