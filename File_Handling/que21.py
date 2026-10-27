# Maintain book records containing book ID, title, author, and availability status.
# Implement operations to: 
# • Add a book.  
# • Search for a book. 
# • Issue a book. 
# • Return a book.  
# • Display available books. 
import os

FILE = "books.txt"

def load_books():
    books = {}
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            for line in file:
                book_id, title, author, status = (
                    line.strip().split(",", 3)
                )
                books[book_id] = [title, author, status]
    return books

def save_books(books):
    with open(FILE, "w") as file:
        for book_id, details in books.items():
            file.write(
                f"{book_id},{details[0]},{details[1]},"
                f"{details[2]}\n"
            )

def add_book(books):
    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("Book ID already exists.")
        return

    title = input("Enter Title: ")
    author = input("Enter Author: ")

    books[book_id] = [title, author, "Available"]
    save_books(books)
    print("Book added successfully.")

def search_book(books):
    book_id = input("Enter Book ID to search: ")
    if book_id in books:
        print(book_id, books[book_id])
    else:
        print("Book not found.")

def issue_book(books):
    book_id = input("Enter Book ID to issue: ")
    if book_id in books and books[book_id][2] == "Available":
        books[book_id][2] = "Issued"
        save_books(books)
        print("Book issued successfully.")
    else:
        print("Book unavailable or not found.")

def return_book(books):
    book_id = input("Enter Book ID to return: ")
    if book_id in books and books[book_id][2] == "Issued":
        books[book_id][2] = "Available"
        save_books(books)
        print("Book returned successfully.")
    else:
        print("Book not issued or not found.")

def display_available(books):
    for book_id, details in books.items():
        if details[2] == "Available":
            print(book_id, details)

books = load_books()

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book(books)
    elif choice == "2":
        search_book(books)
    elif choice == "3":
        issue_book(books)
    elif choice == "4":
        return_book(books)
    elif choice == "5":
        display_available(books)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")