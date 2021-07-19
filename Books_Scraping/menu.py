import logging
from app import book

logger = logging.getLogger('scraping.menu')

USER_CHOICE = """
Enter one of the following:

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'd' to just get the next available book on the catalogue
- 'q' to exit
Enter your Choice: """

def bestbooks():
    logger.debug('finding best 10 books..............')
    best_books = sorted(book, key=lambda x: x.rating * -1)[:10]
    #best_books = sorted(book, key=lambda x: (x.rating * -1,x:price))[:10]
    for books in best_books:
        print(books)


def cheapbooks():
    logger.debug('finding  10 cheapest  books..............')
    cheap_book = sorted(book, key = lambda x: x.price)[:10]
    for books in cheap_book:
        print(books)

book_generator = (x for x in book) #() are used in generator comprehension
def nextbooks():
    logger.debug('finding other books as an option...........')
    print(next(book_generator))


User_Input ={
    'b': bestbooks,
    'c': cheapbooks,
    'd': nextbooks
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ['b','c','d']:
            User_Input[user_input]()
        user_input = input("wanna continue?..if 'yes' press b,c or d according to your choice or 'q' for quiting/'No':")
    logger.debug('Terminating Program......')


menu()
