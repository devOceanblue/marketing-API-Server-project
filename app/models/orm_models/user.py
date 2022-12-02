from sqlalchemy import Integer, Column, TIMESTAMP, FetchedValue, func, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String)
    gender = Column(String)
    balance = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=FetchedValue(),
        server_onupdate=FetchedValue(),
    )

    def __init__(self, user_id, country, gender, balance):
        self.user_id = user_id
        self.country = country
        self.gender = gender
        self.balance = balance
