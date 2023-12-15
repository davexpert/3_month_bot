from aiogram import types, Dispatcher
from config import bot, GROUP_ID
from database.sql_commands import Database

async def ban_users(message: types.Message):
    db = Database()
    user = db.sql_select_ban_user(message.from_user.id)

    if user:
        text = (f"Hello {message.from_user.first_name}\n"
                f"You are in ban list. Violations {user['ban_count']}")

    else:
        text = (f"Hello {message.from_user.first_name}\n"
                f"You are not in list")

    await bot.send_message(
        chat_id=GROUP_ID,
        text=text,
    )

def register_new_ban_user_handler(dp: Dispatcher):
    dp.register_callback_query_handler(ban_users,
                                       lambda call: call.data == "my_ban_count")