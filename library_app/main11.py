# 12. Create a directory structure for a library application with separate packages for: 
# a) Books  
# b) Members 
# c) Transactions
# Each package should contain suitable modules and a main program should combine all functionality. 
from Books.book_details import get_books
from Books.book_search import search_book
from Members.member_details import get_member
from Transactions.issue_return import issue_book, return_book

books = get_books()
member = get_member()

print("--- Library Books ---")
for book in books:
    print(book["id"], book["title"], "-", book["author"])

print("\n--- Member Information ---")
print("Member ID:", member["member_id"])
print("Name:", member["name"])
print("Membership:", member["membership"])

title = input("\nEnter book title to search: ")
result = search_book(books, title)

if result:
    print("Book found:", result["title"])
    print(issue_book(result["title"]))
    print(return_book(result["title"]))
else:
    print("Book not found.")
