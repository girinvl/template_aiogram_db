from typing import List

from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy import update as sqlalchemy_update, delete, literal, sql, exists
from sqlalchemy.future import select
import sqlalchemy as sa

from utils.db_api.create_session import async_db_session, Base
from utils.misc.logging import logging


class BaseModel(Base):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.columns
        values = {
            column.name: getattr(self, column.name)
            for column in primary_key_columns
        }
        values_str = "\n".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True

    created_at = sa.Column(sa.DateTime(True), server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime(True),
                        default=sa.func.now(),
                        onupdate=sa.func.now(),
                        server_default=sa.func.now())


class GetAdditionalMethods:

    @classmethod
    async def create(cls, **kwargs):
        # print('теперь я тут')
        # x = list(map(literal, kwargs.values()))
        # sel = select(*x).where(~exists([cls.id]).where(cls.id == kwargs.get('id')))
        # query = (
        #     sql.insert(cls).from_select(kwargs.keys(), sel)
        # )
        # print(query)
        # await async_db_session.execute(query)
        try:
            async_db_session.add(cls(**kwargs))
            await async_db_session.commit()
        except IntegrityError as e:
            logging.info(e.orig)
            await async_db_session.session.rollback()

    @classmethod
    async def update(cls, id, **kwargs):
        query = (
            sqlalchemy_update(cls).where(cls.id == id).values(**kwargs).execution_options(synchronize_session="fetch")
        )
        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def get(cls, id: int):

        query = select(cls).where(cls.id == id)
        try:
            results = await async_db_session.execute(query)
            (result,) = results.one()
            # await async_db_session.commit()
            return result
        except NoResultFound as e:
            logging.info(e)
            await async_db_session.session.rollback()
            return None

    @classmethod
    async def delete(cls, id: int):
        query = delete(cls).where(cls.id == id)
        await async_db_session.execute(query)
        await async_db_session.commit()
