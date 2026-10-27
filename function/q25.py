# Library management system using dictionaries
books = {}

def add_book(book_id, name):
    books[book_id] = {"name": name, "available": True}
    print("Book added")

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued")
    else:
        print("Book unavailable")

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned")
    else:
        print("Book not found")

def search_book(name):
    for book in books.values():
        if name.lower() in book["name"].lower():
            print(book["name"])

def display_books():
    for book_id, book in books.items():
        status = "Available" if book["available"] else "Issued"
        print(book_id, book["name"], status)

add_book(1, "Python")
add_book(2, "Java")
issue_book(1)
search_book("Python")
return_book(1)
display_books()