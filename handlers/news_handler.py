from aiogram import types, Dispatcher
from scraper.news_scraper import NewsScraper

async def scrape_news(call: types.CallbackQuery):
    scraper = NewsScraper()
    data = scraper.parse_data()
    for url in data[:3]:
        await call.message.answer(
            f"{NewsScraper.PLUS_URL}{url}",
        )

def register_news_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(scrape_news, lambda c: c.data == "news")