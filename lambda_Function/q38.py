# Squares of list elements using map() and lambda
numbers = list(map(int, input("Enter numbers: ").split()))

squares = list(map(lambda x: x ** 2, numbers))

print("Squares =", squares)