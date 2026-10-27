# Pass functions as arguments to another function
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

def calculate(a, b, operation):
    return operation(a, b)

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", calculate(x, y, add))
print("Subtraction:", calculate(x, y, subtract))
print("Multiplication:", calculate(x, y, multiply))
print("Division:", calculate(x, y, divide))