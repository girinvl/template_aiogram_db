from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsApproved(BoundFilter):

    async def check(self, msg: types.Message):
        return True  # or False
