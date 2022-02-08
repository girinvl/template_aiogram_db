from typing import Union

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.db_api.quick_comand import get_user
from utils.db_api.schemas import Users


class UserDb(BaseMiddleware):
    def __init__(self):
        self.user: Union[Users, None] = None
        super(UserDb, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        self.user = await get_user(message.from_user.id)
        data['user_db'] = self.user
