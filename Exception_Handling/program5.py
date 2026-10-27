# Multiple exceptions using try-except-finally
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division =", a / b)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program completed")