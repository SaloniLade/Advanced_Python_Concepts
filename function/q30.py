# Convert decimal to binary using recursion
def decimal_binary(n):
    if n > 1:
        decimal_binary(n // 2)
    print(n % 2, end="")

n = int(input("Enter a decimal number: "))

if n >= 0:
    decimal_binary(n)
else:
    print("Enter a non-negative number")