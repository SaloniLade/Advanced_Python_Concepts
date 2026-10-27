# Add corresponding elements of two lists using map() and lambda
a = list(map(int, input("Enter first list: ").split()))
b = list(map(int, input("Enter second list: ").split()))

if len(a) == len(b):
    result = list(map(lambda x, y: x + y, a, b))
    print("Sum of corresponding elements =", result)
else:
    print("Both lists must have equal lengths.")