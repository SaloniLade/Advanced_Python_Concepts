# Calculate the average of a list of numbers.
def average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(int, input("Enter numbers: ").split()))
print("Average =", average(numbers))