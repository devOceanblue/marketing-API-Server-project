from functools import wraps

from fastapi.logger import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import config

engine = create_engine(
    f"mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db}?charset=utf8mb4"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(SessionLocal)


def get_session(name):
    def wrap(func):
        @wraps(func)
        async def inner(*args, **kwargs):
            with Session() as session:
                with session.begin():
                    kwargs[name] = session
                    return await func(*args, **kwargs)

        return inner

    return wrap
