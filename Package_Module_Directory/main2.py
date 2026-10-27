# Create a module number_utils.py containing functions to check whether a number is prime, palindrome, Armstrong, or perfect. 
# Import the required functions into a main program. 
import number_utils

n = int(input("Enter a number: "))

print("Prime:", number_utils.is_prime(n))
print("Palindrome:", number_utils.is_palindrome(n))
print("Armstrong:", number_utils.is_armstrong(n))
print("Perfect:", number_utils.is_perfect(n))
