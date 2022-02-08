from typing import Union

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api.schemas import Users


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, user_db: Union[Users, None] = None):
    await message.answer(f"Привет, {message.from_user.full_name}!")
