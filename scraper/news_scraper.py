# from parsel import Selector
# import requests
# import asyncio
# import httpx
#
# class NewsScraper:
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0 (Edition Yx GX)',
#         'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#         'Accept-Encoding': 'gzip, deflate, br'
#     }
#
#     MAIN_URL = 'https://animespirit.tv'
#     PLUS_URL = 'https://animespirit.tv'
#
#     def __init__(self):
#         self.links = []
#
#     async def get_html(self, url):
#         async with httpx.AsyncClient() as client:
#             response = await client.get(url, headers=self.headers)
#             print(url)
#             result = self.parse_news(response.text)
#             self.links.extend(result)
#
#     def parse_news(self, response):
#         selector = Selector(text=response)
#         title = selector.xpath('//title/text()').get()
#         news_info = []
#         all_news = selector.xpath('//div[@class="card col-view"]//a//h3/text()').getall()
#         all_links = selector.xpath('//div[@class="custom-poster"]/a/@href').getall()
#
#         return all_links
#
# async def main():
#     scraper = NewsScraper()
#     ######
#     # SYNC
#     # for i in range(1, 6):
#     #     url = f"https://www.prnewswire.com/news-releases/news-releases-list/?page={i}&pagesize=25"
#     #     html = await scraper.get_html(url)
#     ######
#     # ASYNC
#     pages = []
#     throttler = asyncio.Semaphore(5)
#     # for i in range(1, 5):
#     url = f"https://animespirit.tv/page/{i}"
#     task = asyncio.create_task(scraper.get_html(url))
#     pages.append(task)
#
#     await asyncio.gather(*pages)
#
#     # pprint(scraper.links[:5])
#     # print(len(scraper.links))
#
# if __name__ == '__main__':
#     asyncio.run(main())