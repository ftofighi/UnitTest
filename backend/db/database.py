from email.generator import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from core.config import settings

database_url = 'sqlite:///./backend.db'
SQLALCHEMY_DATABASE_URL = database_url
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

"""
this function uses for connect to different database
"""
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally: db.close()


def get_conn():
    engine.connect()
    return engine.url.database
    