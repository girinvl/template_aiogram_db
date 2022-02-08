from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .users_bd import UserDb

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(UserDb())
