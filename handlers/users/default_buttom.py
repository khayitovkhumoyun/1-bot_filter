from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu import menu, menu2
from loader import dp, Bot, bot
from states.PersonState import PersonalData


@dp.message_handler(text='viloyat')
async def form(message: types.Message):
    await message.answer('tanlang', reply_markup=menu)


@dp.message_handler(text='buttom1')
async def form(message: types.Message):
    await message.answer('tanlang', reply_markup=menu2)
