from typing import Union

from aiogram import types
from aiogram.types import CallbackQuery, Message
from data.config import ADMINS

from keyboards.inline.admin_menu_keys import (
    menu_cd,
    categories_keyboard,
    items_keyboard,
    item_keyboard,
)
from loader import dp, db


# Bosh menyu matni uchun handler
@dp.message_handler(text_contains="Kafedralar")
async def show_menu(message: types.Message):
    # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
    await list_categories(message)


# Bosh menyu matni uchun handler
# @dp.message_handler(text="Admin Menu")
# async def show_menu(message: types.Message):
#     # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
#     await list_categories(message)


# Kategoriyalarni qaytaruvchi funksiya. Callback query yoki Message qabul qilishi ham mumkin.
# **kwargs yordamida esa boshqa parametrlarni ham qabul qiladi: (category, subcategory, item_id)
async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    # Keyboardni chaqiramiz
    markup = await categories_keyboard()

    # Agar foydalanuvchidan Message kelsa Keyboardni yuboramiz
    if isinstance(message, Message):
        await message.answer("Kafedrani tanlang", reply_markup=markup)

    # Agar foydalanuvchidan Callback kelsa Callback natbibi o'zgartiramiz
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_text("Fanni tanlang", reply_markup=markup)


# Ost-kategoriyaga tegishli mahsulotlar ro'yxatini yuboruvchi funksiya
async def list_items(callback: CallbackQuery, user_id, category, page_number, **kwargs):
    markup = await items_keyboard(user_id, category, page_number)
    await callback.message.edit_text(text="Mavzular:", reply_markup=markup)


# Biror mahsulot uchun Xarid qilish tugmasini yuboruvchi funksiya
async def show_item(
    callback: CallbackQuery, user_id, category, page_number, item_id, item_link
):
    markup = item_keyboard(user_id, category, page_number, item_id, item_link)

    # Mahsulot haqida ma'lumotni bazadan olamiz
    item = await db.get_product(item_id)
    text = f"Mavzu nomi: {item['name']}\nMavzu linki: https://shorturl.at/{item['link']}\nMavzu izohi: {item['description']}"

    await callback.message.edit_text(text=text, reply_markup=markup)


# Biror mahsulot uchun Delete qilish tugmasini yuboruvchi funksiya
async def delete_item(
    callback: CallbackQuery, user_id, category, page_number, item_id, item_link
):
    await db.delete_product(item_id)
    markup = await items_keyboard(user_id, category, page_number)

    await callback.answer(text=f"Mavzu o'chirildi!", show_alert=True)
    # Mahsulot haqida ma'lumotni bazadan olamiz
    # await callback.answer(cache_time=60)
    await callback.message.edit_text(text=f"Mavzular:", reply_markup=markup)
    # await callback.message.edit_reply_markup(markup)


# Yuqoridagi barcha funksiyalar uchun yagona handler
@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Handlerga kelgan Callback query
    :param callback_data: Tugma bosilganda kelgan ma'lumotlar
    """
    # Foydalanuvchi so'ragan Level (qavat)
    user_id = call.from_user.id
    # Foydalanuvchi so'ragan Level (qavat)
    current_level = callback_data.get("level")

    # Foydalanuvchi so'ragan Kategoriya
    category = callback_data.get("category")

    # Foydalanuvchi so'ragan Kategoriya
    page_number = callback_data.get("page_number")

    # Ost-kategoriya (har doim ham bo'lavermaydi)
    # subcategory = callback_data.get("subcategory")

    # Mahsulot ID raqami (har doim ham bo'lavermaydi)
    item_id = int(callback_data.get("item_id"))
    item_link = callback_data.get("item_link")
    # Har bir Level (qavatga) mos funksiyalarni yozib chiqamiz
    levels = {
        "0": list_categories,  # Kategoriyalarni qaytaramiz
        "1": list_items,  # Mahsulotlarni qaytaramiz
        "2": show_item,  # Mahsulotni ko'rsatamiz
        "3": delete_item,  # Mahsulotni o'chiramiz
    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[current_level]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    await current_level_function(
        call,
        user_id=user_id,
        category=category,
        page_number=page_number,
        item_id=item_id,
        item_link=item_link,
    )
