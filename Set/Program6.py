# Write a program to analyze the vocabulary used in two different books. You need to:
# - Find all unique words used in each book.
# - Identify the common words between both books.
# - Identify words that are unique to each book (not found in the other book).
# - Display the total number of unique words across both books.
# Tasks:

# - Use sets to find the unique words in each text, and perform set operations to find the union, intersection, and differences.



book1 = input("Enter text of book 1: ").lower().split()
book2 = input("Enter text of book 2: ").lower().split()

set1 = set(book1)
set2 = set(book2)

print("Unique words in Book 1:", set1)
print("Unique words in Book 2:", set2)

print("Common words:", set1 & set2)
print("Only in Book 1:", set1 - set2)
print("Only in Book 2:", set2 - set1)

print("Total unique words:", len(set1 | set2))