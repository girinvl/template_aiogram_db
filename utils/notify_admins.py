import logging

from aiogram import Dispatcher

from data.config import ADMINS
from keyboards.inline import keyboard_add_user_inline
from utils.db_api.schemas import Users


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
