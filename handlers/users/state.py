from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu import menu, menu2, menu3
from states.states_grop import RegisterStates
from loader import dp,db
import re


@dp.message_handler(commands='form', state=None)
async def enter_fullname(message: types.Message):
    await message.answer("Iltimos to'liq ism familyangizni kiriting.")
    await RegisterStates.fullName.set()


@dp.message_handler(state=RegisterStates.fullName)
async def fullname(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({'name': name})
    await message.answer("Addres tanlang",reply_markup=menu)
    await RegisterStates.next()


@dp.message_handler(state=RegisterStates.address)
async def address(message: types.Message, state: FSMContext):
    menu = message.text
    if 'qashqadaryo' == menu:
        await message.answer('tuman tanlang', reply_markup=menu2)


    elif 'toshkent' == menu:
        await message.answer('tuman tanlang', reply_markup=menu3)
    await state.update_data({'address': menu})
    await message.answer("Malumotlaringiz qabul qilindi.")
    await RegisterStates.next()

    data = await state.get_data()
    msg = "Ma'lumotlar \n "
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')
    msg += f"Full_Name : {name}\n"
    msg += f"Age : {age}\n"
    msg += f"E-mail : {email}\n"
    msg += f"Phone_number : {phone}\n"
    msg += f"Address : {address}"

    await message.answer(msg)
    await db.add_user()
    await state.finish()

