from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kafedralar"),
            KeyboardButton(text="Takliflar 📝"),
        ],
    ],
    resize_keyboard=True,
)
