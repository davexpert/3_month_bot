from aiogram import executor
from config import dp
from handlers import (
    start,
    questionnaire,
    chat_actions,
    new_ban_user,
    registration,
    profile,
    reference,

)
from database import sql_commands

async def on_startup(_):
    db = sql_commands.Database()
    db.sql_create_tables()



start.register_start_handlers(dp=dp)
questionnaire.register_questionnaire_handler(dp=dp)
new_ban_user.register_new_ban_user_handler(dp=dp)
registration.registration_handlers(dp=dp)
profile.register_profile_handlers(dp=dp)
reference.register_reference_handlers(dp=dp)
chat_actions.register_chat_actions_handlers(dp=dp)


if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
