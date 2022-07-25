"""
Utilities related to database tasks
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


Base = declarative_base()

engine = create_async_engine(settings.database_url, echo=True)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession, future=True)


async def get_db():
    'DI session maker'
    async with async_session() as session:
        yield session
