from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire 🟩",
        callback_data="start_questionnaire"

    )
    registration_button = InlineKeyboardButton(
        "Registration 🔍",
        callback_data="registration"
    )
    profile_button = InlineKeyboardButton(
        "My profile 😎",
        callback_data="my_profile"
    )
    view_profile_button = InlineKeyboardButton(
        "View Profiles 👍🏻👎🏻",
        callback_data="random_profile"
    )
    reference_menu_button = InlineKeyboardButton(
        "Reference Menu 🧲",
        callback_data="reference_menu"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(profile_button)
    markup.add(view_profile_button)
    markup.add(reference_menu_button)
    return markup
async def ban_count_keyboard():
    markup = InlineKeyboardMarkup()
    ban_count_button = InlineKeyboardButton(
        "My ban counter",
        callback_data="my_ban_count"
    )
    markup.add(ban_count_button)
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
async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    anime_button = InlineKeyboardButton(
        "LIKE 👍🏻",
        callback_data=f"like_{owner_tg_id}"
    )
    manga_button = InlineKeyboardButton(
        "DISLIKE 👎🏻",
        callback_data=f"dis_{owner_tg_id}"
    )
    markup.add(anime_button)
    markup.add(manga_button)
    return markup
async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    anime_button = InlineKeyboardButton(
        "Update 🟢",
        callback_data=f"update_profile"
    )
    manga_button = InlineKeyboardButton(
        "Delete ❌",
        callback_data="delete_profile"
    )
    markup.add(anime_button)
    markup.add(manga_button)
    return markup

# async def reference_user_keyboard():
#     markup = InlineKeyboardMarkup()
#     reference_button = InlineKeyboardButton(
#         "Reference Users",
#         callback_data="reference_user"
#     )
#     markup.add(reference_button)
#     return markup
async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    link_button = InlineKeyboardButton(
        "Link",
        callback_data="reference_link"
    )
    reference_button = InlineKeyboardButton(
        "Reference Users",
        callback_data="reference_user"
    )
    markup.add(reference_button)
    markup.add(link_button)
    return markup

