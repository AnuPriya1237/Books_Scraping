import re
import logging
from bs4 import BeautifulSoup
from locators.allbooks_locators import BooksLocator
from parsers.books import BooksParser

logger = logging.getLogger('scraping.to books_pages')


class BooksPage:

    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser ')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        item = self.soup.select(BooksLocator.BOOKS)
        logger.debug(f'fnding all the books locator from `{BooksLocator.BOOKS}`.')
        #print(item)
        return [BooksParser(e) for e in item]

    @property
    def page_count(self):
        logger.debug('finding all the catalogue page details....')
        content = self.soup.select_one(BooksLocator.PAGER).string
        logger.debug(f'Number of catalogue pages`{content}`.')
        expression =  '[0-9]+\s[a-z]+\s([0-9]+)' #or #'page [0-9]+ of ([0-9]+)'

        matcher = re.search(expression,content)
        logger.debug('finding the total number of pages...')
        return int(matcher.group(1))











