import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from const import PROFILE_TEXT
from database.sql_commands import Database


class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    gender = State()
    race = State()
    city = State()
    photo = State()


async def registration_start(call: types.CallbackQuery):
    db = Database()
    tg_id = call.from_user.id
    if db.sql_user_registered(tg_id):
        await bot.send_message(
           chat_id=tg_id,
           text='You are already registered'
        )
        return
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='Send me ur Nickname, please!!!'
        )
    await RegistrationStates.nickname.set()

async def update_profile_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Send me ur Nickname, please!!!'
    )
    await RegistrationStates.nickname.set()

async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Tell me about urself, please!!!'
    )
    await RegistrationStates.next()


async def load_biography(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['biography'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='How old r u?\n'
             'Send me only numeric answer\n'
             'Example: 26, 89, 18\n'
             'Not good: Twenty, Seventeen'
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='I said send me only numeric answer\n'
                 'Re-Registration, ur state of registration is over!!!'
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='What is ur gender'
    )
    await RegistrationStates.next()


async def load_gender(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='What ethnicity are You 👤?'
    )
    await RegistrationStates.next()


async def load_race(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['race'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='In what city do you live🌆?'
    )
    await RegistrationStates.next()


async def load_city(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur photo 😎'
    )
    await RegistrationStates.next()

async def load_photo(message: types.Message,
                     state: FSMContext):
    db = Database()
    print(message.photo)
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )
    print(path.name)
    profile = db.sql_select_profile(
        tg_id=message.from_user.id
    )
    async with state.proxy() as data:
        if not profile:
            db.sql_insert_profile(
                tg_id=message.from_user.id,
                nickname=data['nickname'],
                bio=data['biography'],
                age=data['age'],
                gender=data['gender'],
                race=data['race'],
                city=data['city'],
                photo=path.name
            )
            await bot.send_message(
                chat_id=message.from_user.id,
                text="U have registered successfully 🙌🏻🍾🔥"
            )
        elif profile:
            db.sql_update_profile(
                nickname=data['nickname'],
                bio=data['biography'],
                age=data['age'],
                gender=data['gender'],
                race=data['race'],
                city=data['city'],
                photo=path.name,
                tg_id=message.from_user.id
            )
            await bot.send_message(
                chat_id=message.from_user.id,
                text="U have re-registered successfully 🙌🏻🍾🔥"
            )
        with open(path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    bio=data['biography'],
                    age=data['age'],
                    gender=data['gender'],
                    race=data['race'],
                    city=data['city']
                ),
                parse_mode=types.ParseMode.MARKDOWN
            )
        await state.finish()


def registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_callback_query_handler(
        update_profile_call,
        lambda call: call.data == "update_profile"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )
    dp.register_message_handler(
        load_race,
        state=RegistrationStates.race,
        content_types=['text']
    )
    dp.register_message_handler(
        load_city,
        state=RegistrationStates.city,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )

