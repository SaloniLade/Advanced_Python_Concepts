# Check palindrome using recursion
def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

s = input("Enter a string: ")

if palindrome(s):
    print("Palindrome")
else:
    print("Not a palindrome")