import sqlalchemy as sa
from aiogram.types import User
from sqlalchemy.orm import relationship

from utils.db_api.schemas import GetAdditionalMethods, TimedBaseModel


class Users(TimedBaseModel, GetAdditionalMethods):
    __tablename__ = "users"

    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String)
    is_approved = sa.Column(sa.Boolean, default=False)
    bs = relationship("Record")

    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        x = User(id=self.id)
        return f"""
        id\t-\t{self.id},
        имя\t-\t{x.get_mention(name=self.name)},
        создано\t-\t{self.created_at.strftime('%d.%m.%Y  %H:%M:%S')},
        обновлено\t-\t{self.updated_at.strftime('%d.%m.%Y  %H:%M:%S')}
        """
