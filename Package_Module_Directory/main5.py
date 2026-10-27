# 
# Create a module containing recursive functions for factorial, Fibonacci series, sum of digits, and binary conversion. Import and use these functions from another program. 
import recursive_utils

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    print("Factorial:", recursive_utils.factorial(n))
    print("Fibonacci series:", recursive_utils.fibonacci(n))
    print("Sum of digits:", recursive_utils.sum_of_digits(n))
    print("Binary conversion:", recursive_utils.binary_conversion(n))
