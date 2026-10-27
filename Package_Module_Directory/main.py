# Create a Python module calculator.py containing functions for addition, subtraction, multiplication, and division. 
# Create another program that imports the module and performs calculations based on user input. 
import calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", calculator.add(a, b))
print("Subtraction:", calculator.subtract(a, b))
print("Multiplication:", calculator.multiply(a, b))
print("Division:", calculator.divide(a, b))
