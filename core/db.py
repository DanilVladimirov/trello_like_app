import os

from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

Base = declarative_base()


async def get_session() -> AsyncSession:
    async with AsyncSession(engine) as session:
        yield session
