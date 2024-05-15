from aiogram.dispatcher.filters.state import StatesGroup, State


class OfferData(StatesGroup):
    offer = State()
    status = State()
    offerer = State()
    title = State()
