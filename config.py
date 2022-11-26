import os
from sqlalchemy import create_engine


host = os.getenv("DB_HOST")
db = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")