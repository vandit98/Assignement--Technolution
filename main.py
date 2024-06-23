from book import Book
from user import User
from storage import Storage

class Library:
    def __init__(self):
        self.books = Storage.load_data('books.json')
        self.users = Storage.load_data('users.json')
        self.transactions = Storage.load_data('transactions.json')
        self.checkouts = Storage.load_data('checkouts.json')

    def checkout_book(self, user_id, ISBN):
        # Check if user exists
        user = next((u for u in self.users if u['user_id'] == user_id), None)
        if user is None:
            print(f"Error: User with ID {user_id} not found.")
            return
        
        # Check if book exists and is available
        book = next((b for b in self.books if b['ISBN'] == ISBN), None)
        if book is None:
            print(f"Error: Book with ISBN {ISBN} not found.")
            return
        if not book['availability']:
            print(f"Error: Book with ISBN {ISBN} is not available.")
            return
        
        # Update book availability and add transaction
        book['availability'] = False
        self.transactions.append({
            'user_id': user_id,
            'ISBN': ISBN,
            'action': 'checkout'
        })
        self.checkouts.append({
            'user_id': user_id,
            'ISBN': ISBN
        })
        Storage.save_data('books.json', self.books)
        Storage.save_data('transactions.json', self.transactions)
        Storage.save_data('checkouts.json', self.checkouts)
        print(f"Book with ISBN {ISBN} checked out successfully.")

    def checkin_book(self, user_id, ISBN):
        # Check if user exists
        user = next((u for u in self.users if u['user_id'] == user_id), None)
        if user is None:
            print(f"Error: User with ID {user_id} not found.")
            return
        
        # Check if user has checked out the book
        checkout = next((c for c in self.checkouts if c['user_id'] == user_id and c['ISBN'] == ISBN), None)
        if checkout is None:
            print(f"Error: User with ID {user_id} has not checked out the book with ISBN {ISBN}.")
            return
        
        # Update book availability and add transaction
        book = next((b for b in self.books if b['ISBN'] == ISBN), None)
        if book:
            book['availability'] = True
            self.transactions.append({
                'user_id': user_id,
                'ISBN': ISBN,
                'action': 'checkin'
            })
            self.checkouts = [c for c in self.checkouts if not (c['user_id'] == user_id and c['ISBN'] == ISBN)]
            Storage.save_data('books.json', self.books)
            Storage.save_data('transactions.json', self.transactions)
            Storage.save_data('checkouts.json', self.checkouts)
            print(f"Book with ISBN {ISBN} checked in successfully.")

    def track_availability(self):
        print("Book availability:")
        for book in self.books:
            print(f"Title: {book['title']}, ISBN: {book['ISBN']}, Available: {book['availability']}")

class CLI:
    def __init__(self):
        self.library = Library()

    def main_menu(self):
        while True:
            print("\n==== Library Management System ====")
            print("1. Book Management")
            print("2. User Management")
            print("3. Check Out Book")
            print("4. Check In Book")
            print("5. Track Book Availability")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.handle_book_management()
            elif choice == '2':
                self.handle_user_management()
            elif choice == '3':
                self.handle_check_out()
            elif choice == '4':
                self.handle_check_in()
            elif choice == '5':
                self.library.track_availability()
            elif choice == '6':
                print("Exiting Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def handle_book_management(self):
        while True:
            print("\n==== Book Management ====")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. List Books")
            print("5. Search Book")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.update_book()
            elif choice == '3':
                self.delete_book()
            elif choice == '4':
                self.library.list_books()
            elif choice == '5':
                self.search_book()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def handle_user_management(self):
        while True:
            print("\n==== User Management ====")
            print("1. Add User")
            print("2. Update User")
            print("3. Delete User")
            print("4. List Users")
            print("5. Search User")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.update_user()
            elif choice == '3':
                self.delete_user()
            elif choice == '4':
                self.library.list_users()
            elif choice == '5':
                self.search_user()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def handle_check_out(self):
        user_id = input("Enter user ID: ")
        ISBN = input("Enter ISBN of the book to check out: ")
        self.library.check_out_book(user_id, ISBN)

    def handle_check_in(self):
        user_id = input("Enter user ID: ")
        ISBN = input("Enter ISBN of the book to check in: ")
        self.library.check_in_book(user_id, ISBN)

    def add_book(self):
        title = input("Enter title of the book: ")
        author = input("Enter author of the book: ")
        ISBN = input("Enter ISBN of the book: ")
        Book.add_book(title, author, ISBN)
        print("Book added successfully.")

    def update_book(self):
        ISBN = input("Enter ISBN of the book to update: ")
        author = input("Enter new author of the book: ")
        Book.update_book(ISBN, {'author': author})
        print("Book updated successfully.")

    def delete_book(self):
        ISBN = input("Enter ISBN of the book to delete: ")
        Book.delete_book(ISBN)
        print("Book deleted successfully.")

    def search_book(self):
        title = input("Enter title of the book to search: ")
        found_books = Book.search_book(title=title)
        if found_books:
            print("Found books:")
            for book in found_books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['ISBN']}, Available: {book['availability']}")
        else:
            print("No books found.")

    def add_user(self):
        name = input("Enter name of the user: ")
        user_id = input("Enter user ID: ")
        User.add_user(name, user_id)
        print("User added successfully.")

    def update_user(self):
        user_id = input("Enter user ID to update: ")
        name = input("Enter new name of the user: ")
        User.update_user(user_id, {'name': name})
        print("User updated successfully.")

    def delete_user(self):
        user_id = input("Enter user ID to delete: ")
        User.delete_user(user_id)
        print("User deleted successfully.")

    def search_user(self):
        name = input("Enter name of the user to search: ")
        found_users = User.search_user(name=name)
        if found_users:
            print("Found users:")
            for user in found_users:
                print(f"Name: {user['name']}, User ID: {user['user_id']}")
        else:
            print("No users found.")

#  example usecase
# if __name__ == "__main__":
#     cli = CLI()
#     cli.main_menu()

#  example usecase for library class
# if __name__ == "__main__":
#     library = Library()

#     # Example usage:
#     # Check out a book
#     library.checkout_book('user123', 'ISBN123')

#     # Check in a book
#     library.checkin_book('user123', 'ISBN123')
