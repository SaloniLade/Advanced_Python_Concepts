
def search_book(books, title):
    for book in books:
        if title.lower() in book["title"].lower():
            return book
    return None
