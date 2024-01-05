# from aiogram import types, Dispatcher
# from scraper.news_scraper import NewsScraper
# import asyncio
# async def scrape_news(call: types.CallbackQuery):
#     scraper = NewsScraper()
#     pages = []
#     throttler = asyncio.Semaphore(5)
#     # for i in range(1, 5):
#     url = f"https://animespirit.tv"
#     task = asyncio.create_task(scraper.get_html(url))
#     pages.append(task)
#
#     await asyncio.gather(*pages)
#
#     data = scraper.links
#     for url in data[:5]:
#         await call.message.answer(
#             f"{NewsScraper.PLUS_URL}{url}",
#         )
#
# def register_news_handlers(dp: Dispatcher):
#     dp.register_callback_query_handler(scrape_news, lambda c: c.data == "news")