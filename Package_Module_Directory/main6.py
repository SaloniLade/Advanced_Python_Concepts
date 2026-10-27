# 7. Create a package named mathutils containing:
# a) basic.py – arithmetic operations  
# b) number.py – prime, Armstrong, palindrome functions  
# c) statistics.py – mean, maximum, minimum  
# Create a main program that imports functions from each module. 
from mathutils.basic import add, subtract, multiply, divide
from mathutils.number import is_prime, is_armstrong, is_palindrome
from mathutils.statistics import mean, maximum, minimum

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nArithmetic Operations")
print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))

print("\nNumber Checks")
print("Prime:", is_prime(a))
print("Armstrong:", is_armstrong(a))
print("Palindrome:", is_palindrome(a))

numbers = list(map(int, input(
    "\nEnter numbers separated by spaces: "
).split()))

print("\nStatistics")
print("Mean:", mean(numbers))
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))
