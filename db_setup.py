from sqlalchemy import create_engine

import config

engine = create_engine(f"mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db}?charset=utf8mb4")