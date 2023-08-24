from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")

    # user = await db.get_user(message.from_user.id)
    # print(user)
    # if not user:
    #     print("ha")
    # full_name = message.from_user.full_name
    # username = message.from_user.username
    # telegram_id = message.from_user.id
    # await db.add_user(full_name, username, telegram_id, None, None)


