from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback_add_user = CallbackData('add_user', 'yes_no', 'id')


async def keyboard_add_user_inline(id_user: int):
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[[
            InlineKeyboardButton('Да', callback_data=callback_add_user.new(yes_no='yes', id=id_user)),
            InlineKeyboardButton('Нет', callback_data=callback_add_user.new(yes_no='no', id=id_user)),
        ]]
    )
    return keyboard
