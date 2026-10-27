
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_armstrong(n):
    if n < 0:
        return False
    s = str(n)
    power = len(s)
    return sum(int(digit) ** power for digit in s) == n

def is_perfect(n):
    if n < 2:
        return False
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n
