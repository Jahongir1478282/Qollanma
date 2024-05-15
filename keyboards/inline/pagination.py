from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_pagination_keyboard(page_number, total_pages):
    keyboard = InlineKeyboardMarkup(row_width=3)

    if page_number > 1:
        keyboard.insert(
            InlineKeyboardButton(text="Previous", callback_data=f"prev_page")
        )

    if page_number < total_pages:
        keyboard.insert(InlineKeyboardButton(text="Next", callback_data=f"next_page"))

    return keyboard
