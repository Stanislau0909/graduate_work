from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from env_configs.settings import settings


Base = declarative_base()
engine = create_engine(settings.get_db_uri, echo=settings.DB_ECHO)
async_engine = create_async_engine(settings.get_db_uri_async, echo=settings.DB_ECHO)


def get_session():
    sync_session = sessionmaker(engine, expire_on_commit=False)

    with sync_session() as session:
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


async def get_session_async():
    async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()
