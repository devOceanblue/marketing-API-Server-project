from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(f"mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db}?charset=utf8mb4")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session(
    engine,
    name,
    autoflush=False,
    autocommit=False,
):
    def wrap(func):
        @wraps(func)
        def inner(*args, **kwargs):
            with engine.session_maker(
                autoflush=autoflush, autocommit=autocommit, bind=engine
            ) as session:
                try:
                    kwargs[name] = session
                    func(*args, **kwargs)
                except Exception as e:
                    session.rollback()
                    raise e
        return inner
    return wrap