import requests
import logging

from pages.books_pages import BooksPage

logging.basicConfig(format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    level = logging.DEBUG, #as a developer you can set level as  bebug and see debug messages, but many atimes you can use INFO as well or warning messages are very common for ther users.
                    filename = 'logs.txt')

logger = logging.getLogger('Scraping')
logger.info('Loading books list.....')



page_content = requests.get('https://books.toscrape.com').content
page = BooksPage(page_content)
book = page.books


"""
for book in page.books:
    print(book)
"""

#for extracting data of all the 50 pages of the site.

for i in range(1,page.page_count):
    url = f'https://books.toscrape.com/catalogue/page-{i+1}.html'
    page_content = requests.get(url).content
    logger.debug('Creating Allbook_locators for from page locator....')
    page = BooksPage(page_content)
    book.extend(page.books)

