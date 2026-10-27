# Check whether a string or number is a palindrome.
def palindrome(value):
    value = str(value)
    return value == value[::-1]

s = input("Enter a string or number: ")

if palindrome(s):
    print("Palindrome")
else:
    print("Not a palindrome")