import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()
    await db.create()

    print("Users jadvalini yaratamiz...")
    await db.drop_users()
    await db.create_table_users()
    print("Yaratildi")

    print("Foydalanuvchilarni qo'shamiz")

    await db.add_user("anvar", "sariqdev", 123456789)
    await db.add_user("olim", "olim223", 12341123)
    await db.add_user("1", "1", 131231)
    await db.add_user("1", "1", 23324234)
    await db.add_user("John", "JohnDoe", 4388229)
    print("Qo'shildi")

    users = await db.select_all_users()
    print(f"Barcha foydalanuvchilar: {users}")

    user = await db.select_user(id=5)
    print(f"Foydalanuvchi: {user}")

    #### Mahsulotlar uchun test
    print("Products jadvalini yaratamiz...")
    await db.drop_products()
    await db.create_table_products()
    await db.add_product(
        "tg",
        "Telegram",
        "Channel One",
        "https://t.me/testuchunXJD",
        "Bu kanalda yolgon ma'lumotlar tarqatilayotganligi uchun SPAM berilishi kerak",
    )
    await db.add_product(
        "tg",
        "Telegram",
        "Channel Two",
        "https://t.me/testuchunXJD",
        "Bu kanalda yolgon ma'lumotlar tarqatilayotganligi uchun SPAM berilishi kerak",
    )
    await db.add_product(
        "in",
        "Instagram",
        "Channel One",
        "https://t.me/testuchunXJD",
        "Bu kanalda yolgon ma'lumotlar tarqatilayotganligi uchun SPAM berilishi kerak",
    )
    await db.add_product(
        "in",
        "Instagram",
        "Channel Two",
        "https://t.me/testuchunXJD",
        "Bu kanalda yolgon ma'lumotlar tarqatilayotganligi uchun SPAM berilishi kerak",
    )
    await db.add_product(
        "in",
        "Instagram",
        "Channel Three",
        "https://t.me/testuchunXJD",
        "Bu kanalda yolgon ma'lumotlar tarqatilayotganligi uchun SPAM berilishi kerak",
    )
    await db.add_product(
        "fb",
        "Facebook",
        "Channel One",
        "https://t.me/testuchunXJD",
        "Bu kanalda yolgon ma'lumotlar tarqatilayotganligi uchun SPAM berilishi kerak",
    )
    await db.add_product(
        "fb",
        "Facebook",
        "Channel Two",
        "https://t.me/testuchunXJD",
        "Bu kanalda yolgon ma'lumotlar tarqatilayotganligi uchun SPAM berilishi kerak",
    )
    await db.add_product(
        "fb",
        "Facebook",
        "Channel Three",
        "https://t.me/testuchunXJD",
        "Bu kanalda yolgon ma'lumotlar tarqatilayotganligi uchun SPAM berilishi kerak",
    )
    await db.add_product(
        "fb",
        "Facebook",
        "Channel Four",
        "https://t.me/testuchunXJD",
        "Bu kanalda yolgon ma'lumotlar tarqatilayotganligi uchun SPAM berilishi kerak",
    )

    categories = await db.get_categories()
    print(f"{categories=}")
    print(categories[0]["category_code"])

    product = await db.get_product(1)
    print(f"{product=}")
    product = await db.get_product(5)
    print(f"{product=}")


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
