import re
import logging

from locators.books_page_locators import BooksPageLocator

logger = logging.getLogger('scraping.books')
class BooksParser:

    Rating_number = {
        'One' : 1,
        'Two' : 2,
        'Three' : 3,
        'Four' : 4,
        'Five' : 5,
    }

    def __init__(self, parent):
        logger.debug('Values of page content passed over here.....')
        self.parent = parent


    def __repr__(self):
        logger.info('displaying required data...... ')
        if self.rating == 1:
            return f'<book: {self.name}, £{self.price}, {self.rating} star>'
        return f'<book: {self.name}, £{self.price}, {self.rating} stars>'



    @property
    def name(self):
        locators = BooksPageLocator.NAME_LOCATOR
        logger.info('Title of the book....')
        return self.parent.select_one(locators).attrs['title']
    @property
    def rating(self):
        locators = BooksPageLocator.RATING_LOCATOR
        rate = self.parent.select_one(locators).attrs['class']
        classes = [e for e in rate if e != 'star-rating']
        Ratings = BooksParser.Rating_number.get(classes[0])
        logger.debug('Ratings of the book as per page content...........')
        return Ratings

    @property
    def link(self):
        locators = BooksPageLocator.LINK_LOCATOR
        logger.debug('Particular book link.........')
        return self.parent.select_one(locators).attrs['href']

    @property
    def price(self):
        locators = BooksPageLocator.PRICE_LOCATOR
        cost = self.parent.select_one(locators).string

        expression = '\£([0-9]+\.[0-9]+)'
        price_item = re.search(expression, cost)
        pitem = price_item.group(1)
        logger.debug(f'book price`{pitem}` as per page content')
        return float(pitem)


