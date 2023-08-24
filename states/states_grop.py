from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterStates(StatesGroup):
    fullName = State()
    address = State()