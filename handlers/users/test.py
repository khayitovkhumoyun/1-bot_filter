from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import filters
from loader import dp


email_regex = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
phone_regex  = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

@dp.message_handler(filters.Regexp(phone_regex))
async def phone(message:types.Message):
    await message.answer('tel qabul qilindi')\

@dp.message_handler(filters.Regexp(email_regex))
async def phone(message:types.Message):
    await message.answer('email qabul qilindi')