from book import Book

def input_book_data() -> Book:
    title = input("Введите название тайтла: ")
    author = input("Введите имя автора: ")
    publication_year = input("Введите дату выхода поста в формате dd.MM.YYYY ")
    genre = input("Введите жанр тайтла: ")
    answer = input("Прочитан ли тайтл? 1 - да 0 - нет ")
    if answer == 1:
        is_read = True
    else:
        is_read = False

    return Book(
        title=title,
        author=author,
        publication_year=publication_year,
        genre=genre,
        is_read=is_read,
    )

def add_book_to_end(books: list[Book], new_book: Book):
    books.append(new_book)

def print_book_header():
    print(f"{'ИД':<5}{'Название':<25}{'Автор':<25}{'Год публикации':<25}{'Жанр':<25}{'Прочитан':<25}")

def print_one_book(book: Book):
    print(
        f"{book.id:<5}{book.title:<25}{book.author:<25}{book.publication_year:<25}{book.genre:<25}{book.is_read:<25}"
    )

def print_books(books: list[Book]):
    print_book_header()

    for book in books:
        print_one_book(book)