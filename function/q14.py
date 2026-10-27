# Count how many times an element occurs in a list.
def count_occurrences(lst, element):
    return lst.count(element)

lst = list(map(int, input("Enter list elements: ").split()))
element = int(input("Enter element to count: "))
print("Occurrences =", count_occurrences(lst, element))