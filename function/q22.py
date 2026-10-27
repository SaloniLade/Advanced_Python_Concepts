# Find the minimum, maximum, sum, and average of a list.
def list_operations(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    avg = total / len(numbers)

    return minimum, maximum, total, avg

numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) > 0:
    minimum, maximum, total, avg = list_operations(numbers)

    print("Minimum =", minimum)
    print("Maximum =", maximum)
    print("Sum =", total)
    print("Average =", avg)
else:
    print("Please enter at least one number.")