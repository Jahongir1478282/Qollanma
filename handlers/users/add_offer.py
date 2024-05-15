from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp, db
from states.add_offer import OfferData
from keyboards.inline.offers_key import offers_key, offers_status


@dp.message_handler(text="Takliflar 📝")
async def enter_test(message: types.Message):
    await message.answer("Takliflar menusi", reply_markup=offers_key)


@dp.callback_query_handler(text="add_offer")
async def add_channel(call: types.CallbackQuery):
    await call.message.answer(f"Taklifingizni kiriting:")
    await OfferData.offer.set()


@dp.message_handler(state=OfferData.offer)
async def answer_name(message: types.Message, state: FSMContext):
    offer = message.text
    await state.update_data({"offer": offer})
    await state.update_data({"offerer": message.from_user.username})
    await state.update_data({"title": message.from_user.full_name})
    await message.answer(
        f"\n<blockquote>{offer}</blockquote>\n\nSiz yuqoridagi bermoqchisiz\nushbu taklifingizni <b>tasdiqlang</b> yoki <b>bekor</b> qiling:",
        reply_markup=offers_status,
        parse_mode="HTML",
    )
    await OfferData.next()


@dp.callback_query_handler(text="cancel", state=OfferData.status)
async def answer_description(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Taklifingizni bekor qildingiz!")
    await state.finish()


@dp.callback_query_handler(text="approve", state=OfferData.status)
async def answer_description(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    offer = data.get("offer")
    offerer = data.get("offerer")
    title = data.get("title")
    await call.message.delete()
    await db.add_offer(title, offer, offerer)
    await call.message.answer("Taklifingiz yuborildi!")

    # State dan chiqaramiz
    # 1-variant
    await state.finish()

    # 2-variant
    # await state.reset_state()

    # 3-variant. Ma`lumotlarni saqlab qolgan holda
    # await state.reset_state(with_data=False)
