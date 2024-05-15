from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback, book_callback

# 1-usul.
offers_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Taklif qoldirish 💭", callback_data="add_offer"),
        ],
        # [
        #     InlineKeyboardButton(
        #         text="Telegram channel 2", callback_data="second_channel"
        #     ),
        # ],
        # [
        #     InlineKeyboardButton(
        #         text="Telegram channel 3", callback_data="third_channel"
        #     ),
        # ],
        # [
        #     InlineKeyboardButton(
        #         text="Telegram channel 4", callback_data="fourth_channel"
        #     ),
        # ],
        # [
        #     InlineKeyboardButton(
        #         text="Telegram channel 5", callback_data="fiveth_channel"
        #     ),
        # ],
    ]
)
offers_status = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tasdiqlash ✅", callback_data="approve"),
            InlineKeyboardButton(text="Bekor qilish ⛔️", callback_data="cancel"),
        ],
        # [
        #     InlineKeyboardButton(
        #         text="Telegram channel 2", callback_data="second_channel"
        #     ),
        # ],
        # [
        #     InlineKeyboardButton(
        #         text="Telegram channel 3", callback_data="third_channel"
        #     ),
        # ],
        # [
        #     InlineKeyboardButton(
        #         text="Telegram channel 4", callback_data="fourth_channel"
        #     ),
        # ],
        # [
        #     InlineKeyboardButton(
        #         text="Telegram channel 5", callback_data="fiveth_channel"
        #     ),
        # ],
    ]
)
