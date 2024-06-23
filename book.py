from storage import Storage

class Book:
    def __init__(self, title, author, ISBN, availability=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability

    @staticmethod
    def add_book(title, author, ISBN):
        new_book = {
            'title': title,
            'author': author,
            'ISBN': ISBN,
            'availability': True
        }
        books = Storage.load_data('books.json')
        books.append(new_book)
        Storage.save_data('books.json', books)

    @staticmethod
    def update_book(ISBN, updated_data):
        books = Storage.load_data('books.json')
        for book in books:
            if book['ISBN'] == ISBN:
                book.update(updated_data)
                break
        Storage.save_data('books.json', books)

    @staticmethod
    def delete_book(ISBN):
        books = Storage.load_data('books.json')
        books = [book for book in books if book['ISBN'] != ISBN]
        Storage.save_data('books.json', books)

    @staticmethod
    def list_books():
        books = Storage.load_data('books.json')
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['ISBN']}, Available: {book['availability']}")

    @staticmethod
    def search_book(**kwargs):
        books = Storage.load_data('books.json')
        found_books = []
        for book in books:
            if all(book[k] == v for k, v in kwargs.items()):
                found_books.append(book)
        return found_books

### Example Usage
# if __name__ =="__main__":
#     # Adding a new book
#     Book.add_book('Book1', 'Author1', '123')

#     # Listing all books
#     print("Listing all books:")
#     Book.list_books()

#     # Updating a book
#     Book.update_book('123', {'author': 'NewAuthor'})

#     # Deleting a book
#     Book.delete_book('123')

#     # Searching for books
#     found_books = Book.search_book(title='Book1')
#     print("Found books:")
#     for book in found_books:
#         print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['ISBN']}, Available: {book['availability']}")
