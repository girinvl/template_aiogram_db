import typing

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, session
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from data import config

Base = declarative_base()


class AsyncDatabaseSession:
    def __init__(self):
        self.session: typing.Union[Session, None] = None
        self._engine = None

    def __getattr__(self, name):
        return getattr(self.session, name)

    async def init(self):
        self._engine = create_async_engine(config.POSTGRES_URI, echo=False,)

        self.session: Session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )()

    async def create_all(self):
        async with self._engine.begin() as conn:
            # await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


async_db_session = AsyncDatabaseSession()
