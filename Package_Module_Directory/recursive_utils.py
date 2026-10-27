
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    series = fibonacci(n - 1)
    series.append(series[-1] + (series[-2] if len(series) > 1 else 1))
    return series


def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def binary_conversion(n):
    if n < 0:
        return "-" + binary_conversion(-n)
    if n < 2:
        return str(n)
    return binary_conversion(n // 2) + str(n % 2)
