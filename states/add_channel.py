from aiogram.dispatcher.filters.state import StatesGroup, State


class PersonalData(StatesGroup):
    social = State()
    name = State()
    link = State()
    desc = State()
