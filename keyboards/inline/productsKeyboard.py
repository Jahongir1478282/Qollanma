from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback, book_callback

# 1-usul.
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Telegram channel 1", callback_data="first_channel"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Telegram channel 2", callback_data="second_channel"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Telegram channel 3", callback_data="third_channel"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Telegram channel 4", callback_data="fourth_channel"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Telegram channel 5", callback_data="fiveth_channel"
            ),
        ],
    ]
)
categoryMenu2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Telegram channel 1 ✅", callback_data="first_channel"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Telegram channel 2", callback_data="second_channel"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Telegram channel 3", callback_data="third_channel"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Telegram channel 4", callback_data="fourth_channel"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Telegram channel 5", callback_data="fiveth_channel"
            ),
        ],
    ]
)


conditionMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Shart 1", url="https://t.me/testuchunXJD"),
        ],
        [
            InlineKeyboardButton(text="Shart 2", url="https://t.me/testuchunXJD"),
        ],
        [
            InlineKeyboardButton(text="Shart 3", url="https://t.me/testuchunXJD"),
        ],
        [
            InlineKeyboardButton(text="Shart 4", url="https://t.me/testuchunXJD"),
        ],
        [
            InlineKeyboardButton(text="Shart 5", url="https://t.me/testuchunXJD"),
        ],
    ]
)

reportMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Oylik hisobot", url="https://t.me/testuchunXJD"),
        ],
        [
            InlineKeyboardButton(
                text="Haftalik hisobot", url="https://t.me/testuchunXJD"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Kunlik hisobot", url="https://t.me/testuchunXJD"
            ),
        ],
    ]
)

instructionMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram 🟢", callback_data="tg"),
            InlineKeyboardButton(text="Instagram 🔴", callback_data="in"),
        ],
        [
            InlineKeyboardButton(text="Facebook 🔵", callback_data="fa"),
            InlineKeyboardButton(text="TikTok ⚪️", callback_data="tt"),
        ],
        [
            InlineKeyboardButton(text="YouTube 🔻", callback_data="yt"),
            InlineKeyboardButton(text="Odnoklassniki 🟠", callback_data="ok"),
        ],
    ]
)


# 2-usul
coursesMenu = InlineKeyboardMarkup(row_width=1)

python = InlineKeyboardButton(
    text="🐍 Python Dasturlash Asoslari",
    callback_data=course_callback.new(item_name="python"),
)
coursesMenu.insert(python)

django = InlineKeyboardButton(
    text="🌐 Django Web Dasturlash",
    callback_data=course_callback.new(item_name="django"),
)
coursesMenu.insert(django)

telegram = InlineKeyboardButton(
    text="🤖 Mukammal Telegram bot", callback_data="course:telegram"
)
coursesMenu.insert(telegram)

algorithm = InlineKeyboardButton(
    text="📈 Ma'lumotlar Tuzilmasi va Algoritmlar", callback_data="course:algorithm"
)
coursesMenu.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
coursesMenu.insert(back_button)

# 3 - usul

books = {
    "Python. Dasturlash asoslari": "python_book",
    "C++. Dasturlash tili": "cpp_book",
    "Mukammal Dasturlash. JavaScript": "js_book",
}

booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(
        InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value))
    )
booksMenu.insert(back_button)

# Har bir kurs uchun tugma
telegram_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Xarid qilish", url="https://mohirdev.uz/courses/telegram/"
            )
        ]
    ]
)

algoritm_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Ko'rish", url="https://mohirdev.uz/courses/algoritmlar/"
            )
        ]
    ]
)
