from aiogram import types, Dispatcher
from config import bot, GROUP_ID, ADMIN_ID
from profanity_check import predict, predict_prob
from database.sql_commands import Database
from keyboards.inline_buttons import ban_count_keyboard
import sqlite3
from datetime import timedelta, datetime


async def chat_messages(message: types.Message):
    db = Database()
    if message.chat.id == int(GROUP_ID):

        ban_word_predict_prob = predict_prob([message.text])
        print(ban_word_predict_prob)
        if ban_word_predict_prob[0] > 0.5:
            user = db.sql_select_ban_user(
                tg_id=message.from_user.id

            )
            print(user)
            if not user:
                db.sql_insert_new_ban_user(
                    tg_id=message.from_user.id
                )

            elif user['count'] > 3:
                if user['telegram_id'] == int(ADMIN_ID):
                    pass
                else:
                    await bot.send_message(
                        chat_id=message.chat.id,
                        text="You are banned"
                    )
                # await bot.ban_chat_member(
                #     chat_id=message.chat.id,
                #     user_id=message.from_user.id,
                #     until_date=datetime.now() + timedelta(seconds=30)
                # )
            else:
                db.sql_update_ban_user_count(
                    tg_id=message.from_user.id
                )

            await message.delete()
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"It is not allowed to curse in this grup\n"
                     f"User: {message.from_user.first_name}\n"
                     f"In third you will be banned"
            )












def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_messages)