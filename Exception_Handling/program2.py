# ValueError exception

try:
    n = int(input("Enter a number: "))
    print("Number =", n)

except ValueError:
    print("Please enter a valid integer")