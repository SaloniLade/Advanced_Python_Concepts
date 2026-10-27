# Recursive binary search
# The list must be sorted before searching.
def binary_search(a, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binary_search(a, low, mid - 1, key)
    else:
        return binary_search(a, mid + 1, high, key)

a = list(map(int, input("Enter sorted numbers: ").split()))
key = int(input("Enter element to search: "))

result = binary_search(a, 0, len(a) - 1, key)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)