from book import Book
from book_functions import *

global_book_id = 0

def get_next_book_id() -> int:
    global global_book_id
    global_book_id += 1

    return global_book_id

books: list[Book] = []

new_book = input_book_data()
new_book.id = get_next_book_id()

add_book_to_end(books, new_book)

new_book = input_book_data()
new_book.id = get_next_book_id()

add_book_to_end(books, new_book)

print_books(books)