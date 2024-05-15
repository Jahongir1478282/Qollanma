import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import db
from data.config import ADMINS

# Turli tugmalar uchun CallbackData-obyektlarni yaratib olamiz
menu_cd = CallbackData(
    "show_menu", "level", "user_id", "category", "page_number", "item_id", "item_link"
)
buy_item = CallbackData("buy", "item_id")
add_channel = CallbackData("add", "category")
page_size = 10


# Quyidagi funksiya yordamida menyudagi har bir element uchun calbback data yaratib olinadi
# Agar mahsulot kategoriyasi, ost-kategoriyasi va id raqami berilmagan bo'lsa 0 ga teng bo'ladi
def make_callback_data(
    level, user_id=0, category="0", page_number="1", item_id="0", item_link=""
):
    return menu_cd.new(
        level=level,
        user_id=user_id,
        category=category,
        page_number=page_number,
        item_id=item_id,
        item_link=item_link,
    )


# Bizning menu 3 qavat (LEVEL) dan iborat
# 0 - Kategoriyalar
# 1 - Ost-kategoriyalar
# 2 - Mahsulotlar
# 3 - Yagona mahsulot


# Kategoriyalar uchun keyboardyasab olamiz
async def categories_keyboard():
    # Eng yuqori 0-qavat ekanini ko'rsatamiz
    CURRENT_LEVEL = 0

    # Keyboard yaratamiz
    markup = InlineKeyboardMarkup(row_width=1)

    # Bazadagi barcha kategoriyalarni olamiz
    categories = await db.get_categories()
    # Har bir kategoriya uchun quyidagilarni bajaramiz:
    for category in categories:
        # Kategoriyaga tegishli mahsulotlar sonini topamiz
        number_of_items = await db.count_socials(category["category_code"])

        # Tugma matnini yasab olamiz
        button_text = f"{category['category_name']} ({number_of_items} dona)"

        # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1, category=category["category_code"]
        )

        # Tugmani keyboardga qo'shamiz
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Keyboardni qaytaramiz
    return markup


# Ostkategoriyaga tegishli mahsulotlar uchun keyboard yasaymiz
async def items_keyboard(user_id, category, page_number):
    CURRENT_LEVEL = 1
    page_int = int(page_number)
    markup = InlineKeyboardMarkup(row_width=1)
    # Ost-kategorioyaga tegishli barcha mahsulotlarni olamiz
    data = await db.get_socials(category)
    items = await pagination(data, page_int)
    for item in items:
        # Tugma matnini yasaymiz
        button_text = f"{item['name']}"
        item_link = item["link"]
        new_item_link = item_link.replace(":", "*")
        # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1,
            category=category,
            page_number=page_number,
            item_id=item["id"],
            item_link=new_item_link,
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # PAGINATION BUTTONS
    prev = (
        make_callback_data(CURRENT_LEVEL, category=category, page_number=page_int - 1)
        if page_int > 1
        else "stop_prev"
    )
    next = (
        make_callback_data(CURRENT_LEVEL, category=category, page_number=page_int + 1)
        if page_int < (len(data) + page_size - 1) // page_size
        else "stop_next"
    )

    markup.row(
        InlineKeyboardButton(text="⬅️ Oldingi", callback_data=prev),
        InlineKeyboardButton(
            text=f"{page_number} / {(len(data) + page_size - 1 ) // page_size}",
            callback_data="opo",
        ),
        InlineKeyboardButton(text="Keyingi ➡️", callback_data=next),
    )
    # markup.row()
    if str(user_id) in ADMINS:
        markup.row(
            # Kanal qo 'shish tugmasi
            InlineKeyboardButton(
                text="Kanal qo'shish ➕", callback_data=add_channel.new(category)
            ),
            # Ortga qaytish tugmasi
            InlineKeyboardButton(
                text="Ortga ↩️",
                callback_data=make_callback_data(
                    level=CURRENT_LEVEL - 1, category=category
                ),
            ),
        )
    else:
        markup.row(
            # Ortga qaytish tugmasi
            InlineKeyboardButton(
                text="Ortga ↩️",
                callback_data=make_callback_data(
                    level=CURRENT_LEVEL - 1, category=category
                ),
            ),
        )

    return markup


# Berilgan mahsulot uchun Xarid qilish va Ortga yozuvlarini chiqaruvchi tugma keyboard
def item_keyboard(user_id, category, page_number, item_id, item_link):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(
        InlineKeyboardButton(
            text=f"Kanalga o'tish", url=f"https://shorturl.at/{item_link}"
        )
    )
    if str(user_id) in ADMINS:
        markup.row(
            InlineKeyboardButton(
                text="❌ Delete",
                callback_data=make_callback_data(
                    level=CURRENT_LEVEL + 1,
                    user_id=user_id,
                    category=category,
                    item_id=item_id,
                ),
            )
        )

    markup.row(
        InlineKeyboardButton(
            text=f"Ortga ↩️",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1, category=category, page_number=page_number
            ),
        )
    )
    return markup


async def pagination(data, page_number):
    total_items = len(data)
    total_pages = (total_items + page_size - 1) // page_size
    try:
        if 1 <= int(page_number) <= total_pages:
            start_index = (page_number - 1) * page_size
            end_index = page_number * page_size
            page_data = data[start_index:end_index]
            return page_data
        else:
            return []
    except ValueError:
        print("Error")
