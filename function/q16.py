# Find the second-largest number in a list.
def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()

    if len(unique) < 2:
        return "No second-largest element"

    return unique[-2]

numbers = list(map(int, input("Enter numbers: ").split()))
print("Second largest =", second_largest(numbers))