# Library Management System

This Python application is a command-line based Library Management System. It allows users to manage books, users, perform check-in and check-out operations, track book availability, and log transactions. The system is designed with object-oriented principles and uses file-based storage for data persistence.

## Features

1. **Manage Books**:
   - Add, update, delete, list, and search books by title, author, or ISBN.

2. **Manage Users**:
   - Add, update, delete, list, and search users by name or user ID.

3. **Check-out and Check-in Books**:
   - Allow users to borrow and return books, updating availability status accordingly.

4. **Track Book Availability**:
   - Display current availability (checked in or checked out) of all books.

5. **Logging**:
   - Simple logging of operations such as book check-out and check-in.

6. **Object-Oriented Design**:
   - Classes (`Book`, `User`, `Library`) with clear responsibilities and relationships.

7. **File-Based Storage**:
   - Data (books, users, transactions, checkouts) stored in JSON format (`books.json`, `users.json`, etc.) for reliability and persistence.

8. **CLI Interface**:
   - Command-line interface for user interaction, providing a friendly and intuitive way to manage the library.

## Usage

1. **Installation**:
   - Clone the repository:
     ```
     git clone https://github.com/vandit98/Assignement--Technolution.git
     ```
   - Install dependencies (if any).

2. **Running the Application**:
   - Navigate to the project directory.
   - Run `python main.py` to start the CLI interface.

3. **Commands**:
   - Follow the prompts to manage books and users, perform check-in and check-out operations, and track book availability.

## Example

```bash
# Example usage to check out a book
python main.py
> checkout user123 ISBN123

# Example usage to check in a book
> checkin user123 ISBN123
