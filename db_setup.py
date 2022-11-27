from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, scoped_session

import config

connect_url = URL.create(
    "mysql+pymysql",
    username=config.user,
    password=config.password,
    host=config.host,
    port=config.port,
    database=config.db,
)

engine = create_engine(connect_url)

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
