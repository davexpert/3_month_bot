from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire 🟩",
        callback_data="start_questionnaire"

    )
    markup.add(questionnaire_button)
    return markup

async def start_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    anime_button = InlineKeyboardButton(
        "Anime 🤘",
        callback_data="anime"
    )
    manga_button = InlineKeyboardButton(
        "Manga 😎",
        callback_data="manga"
    )
    markup.add(anime_button)
    markup.add(manga_button)
    return markup

async def start_questionnaire_keyboard_2():
    markup = InlineKeyboardMarkup()
    fruits_button = InlineKeyboardButton(
        "Fruits 🍎",
        callback_data="fruits"
    )
    vegetables_button = InlineKeyboardButton(
        "Vegetables 🍅",
        callback_data="vegetables"
    )
    markup.add(fruits_button)
    markup.add(vegetables_button)
    return markup

async def start_questionnaire_keyboard_3():
    markup = InlineKeyboardMarkup()
    books_button = InlineKeyboardButton(
        "Books 📚",
        callback_data="books"
    )
    movies_button = InlineKeyboardButton(
        "Movies 🎬",
        callback_data="movies"
    )
    markup.add(books_button)
    markup.add(movies_button)
    return markup