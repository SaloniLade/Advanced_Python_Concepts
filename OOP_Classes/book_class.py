
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print("Book returned successfully.")
        else:
            print("Book was not borrowed.")

    def show_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", "Borrowed" if self.is_borrowed else "Available")


book = Book("Python Programming", "John Smith")

book.show_details()
book.borrow_book()
book.show_details()
book.return_book()
book.show_details()
