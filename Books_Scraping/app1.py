""" This is asynchronous version of app.py of book_scraping.py"""


import aiohttp
import async_timeout
import asyncio
import requests
import logging
import time
from pages.books_pages import BooksPage


logging.basicConfig(format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    level = logging.DEBUG, #as a developer you can set level as  debug and see debug messages, but many atimes you can use INFO as well or warning messages are very common for ther users.
                    filename = 'logs.txt')

logger = logging.getLogger('Scraping')
logger.info('Loading books list.....')


page_content = requests.get('https://books.toscrape.com').content
page = BooksPage(page_content)
book = page.books

#Using asynchronous python

async def fetch_link(session, url):
    start_time = time.time()
    async with async_timeout.timeout(10):
        async with  session.get(url) as response:
            print(f'time taken:{start_time  - time.time()}')
            return await response.text()


async def multiple_page(loop, *urls):
    task = []
    async with aiohttp.ClientSession(loop = loop) as session:
        for url in urls:
            task.append(fetch_link(session, url))
        p = asyncio.gather(*task)
        return await p


loop = asyncio.get_event_loop()
url = [f'https://books.toscrape.com/catalogue/page-{i+1}.html' for i in range(1,page.page_count)]
pages = loop.run_until_complete(multiple_page(loop, *url))



for pagess in pages:
    page = BooksPage(pagess)
    book.extend(page.books)




