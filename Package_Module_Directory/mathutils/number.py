
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    if n < 0:
        return False
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
