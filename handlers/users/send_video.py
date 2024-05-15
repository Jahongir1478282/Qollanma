from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot

instructions = {
    "tg": "Telegram",
    "in": "Istagram",
    "fa": "Facebook",
    "tt": "TikTok",
    "yt": "YouTube",
    "ok": "OK",
}


@dp.callback_query_handler()
async def send_video(call: types.CallbackQuery):
    for instruction in instructions:
        if call.data == instruction:
            video_file = InputFile(path_or_bytesio=f"data/videos/{instruction}.mp4")
            await call.message.answer_video(
                video_file,
                caption=f"{instructions[instruction]} kannallar bo'yicha qo'llanma",
            )
    await call.answer(cache_time=60)


# @dp.callback_query_handler(text="instruction_tg")
# async def send_video(call: types.CallbackQuery):
#     video_file = InputFile(path_or_bytesio="data/videos/video01.mp4")
#     await call.message.answer_video(video_file, caption=f"Telegram kannallar bo'yicha qo'llanma")
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="instruction_in")
# async def send_video(call: types.CallbackQuery):
#     video_file = InputFile(path_or_bytesio="data/videos/video01.mp4")
#     await call.message.answer_video(video_file, caption="Instagram ijtimoiy tarmog'i bo'yicha qo'lanma")
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="instruction_fa")
# async def send_video(call: types.CallbackQuery):
#     video_file = InputFile(path_or_bytesio="data/videos/video01.mp4")
#     await call.message.answer_video(video_file, caption="Facebook ijtimoiy tarmog'i bo'yicha qo'lanma")
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="instruction_tt")
# async def send_video(call: types.CallbackQuery):
#     video_file = InputFile(path_or_bytesio="data/videos/video01.mp4")
#     await call.message.answer_video(video_file, caption="TikTok ijtimoiy tarmog'i bo'yicha qo'lanma")
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="instruction_yt")
# async def send_video(call: types.CallbackQuery):
#     video_file = InputFile(path_or_bytesio="data/videos/video01.mp4")
#     await call.message.answer_video(video_file, caption="Youtube ijtimoiy tarmog'i bo'yicha qo'lanma")
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="instruction_ok")
# async def send_video(call: types.CallbackQuery):
#     video_file = InputFile(path_or_bytesio="data/videos/video01.mp4")
#     await call.message.answer_video(video_file, caption="Odnoklassniki ijtimoiy tarmog'i bo'yicha qo'lanma")
#     await call.answer(cache_time=60)
