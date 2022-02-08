import datetime
import logging
from typing import Union

import sqlalchemy as sa
from sqlalchemy import func, extract
from sqlalchemy.future import select
from sqlalchemy.sql.elements import and_

from utils.db_api.create_session import async_db_session
from utils.db_api.schemas import GetAdditionalMethods, TimedBaseModel


class Record(TimedBaseModel, GetAdditionalMethods):
    __tablename__ = "record"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    users_id = sa.Column(sa.ForeignKey("users.id"))
    amount = sa.Column(sa.Integer, nullable=False)
