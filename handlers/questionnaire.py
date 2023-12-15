import sqlite3
from aiogram import types, Dispatcher
from config import bot
from keyboards import inline_buttons

async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Anime or Manga",
        reply_markup=await inline_buttons.start_questionnaire_keyboard()
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Fruits 🍎 or Vegetables 🍅",
        reply_markup=await inline_buttons.start_questionnaire_keyboard_2()
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Books 📚 or Movies 🎬",
        reply_markup=await inline_buttons.start_questionnaire_keyboard_3()
    )
async def anime_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Yee ANIME for life",
    )
async def manga_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Manga is boring...",
    )

async def fruits_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="I also love Fruits",
    )
async def vegetables_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Veggies keep you healthy",
    )
async def books_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Books open up new worlds!",
    )

async def movies_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Movies bring stories to life!",
    )

async def my_ban_count(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Ban count"
    )
def register_questionnaire_handler(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(anime_call,
                                       lambda call: call.data == "anime")
    dp.register_callback_query_handler(manga_call,
                                       lambda call: call.data == "manga")
    dp.register_callback_query_handler(fruits_call,
                                       lambda call: call.data == "fruits")
    dp.register_callback_query_handler(vegetables_call,
                                       lambda call: call.data == "vegetables")
    dp.register_callback_query_handler(books_call,
                                       lambda call: call.data == "books")
    dp.register_callback_query_handler(movies_call,
                                       lambda call: call.data == "movies")
