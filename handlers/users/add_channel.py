from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboards.default.startMenuKeys import menuStart
from loader import dp, db
from states.add_channel import PersonalData
from data.config import ADMINS
from keyboards.inline.admin_menu_keys import add_channel

mappings = {
    "ax": "Axborot xavfsizligi",
    "kk": "Kiberxavfsizlik va kriminalistika",
    "cr": "Kriptologiya",
}


@dp.message_handler(Command("add"), user_id=ADMINS, state=None)
async def enter_test(message: types.Message):
    await message.answer("Ijtimoiy tarmoq nomi", reply_markup=menuStart)
    await PersonalData.social.set()


@dp.callback_query_handler(add_channel.filter())
async def add_channel(call: types.CallbackQuery, callback_data: dict, state=FSMContext):
    category = str(callback_data.get("category"))
    await call.message.answer(f"Fan nomini kiriting:")
    await PersonalData.name.set()
    await state.update_data({"social": category})


@dp.message_handler(state=PersonalData.name)
async def answer_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await message.answer("Mavzu linkini kiriting:")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.link)
async def answer_link(message: types.Message, state: FSMContext):
    link = message.text
    await state.update_data({"link": link})
    await message.answer("Mavzu izohi")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.desc)
async def answer_description(message: types.Message, state: FSMContext):
    desc = message.text
    await state.update_data({"desc": desc})
    data = await state.get_data()
    social_code = data.get("social")
    social = mappings[social_code]
    name = data.get("name")
    link = data.get("link")
    desc = data.get("desc")

    await db.add_product(social_code, social, name, link, desc)
    await message.answer("Kanal bazaga qo'shildi", reply_markup=menuStart)

    # State dan chiqaramiz
    # 1-variant
    await state.finish()

    # 2-variant
    # await state.reset_state()

    # 3-variant. Ma`lumotlarni saqlab qolgan holda
    # await state.reset_state(with_data=False)
