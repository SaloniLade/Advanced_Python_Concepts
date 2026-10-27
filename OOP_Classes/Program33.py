# Write a program to define a class Calculator that contains a method called add() to perform addition.

# Requirements:
# 1. The add() method should be able to:
#    - Add two numbers if only two arguments are provided.
#    - Add three numbers if three arguments are provided.
#    - Add four numbers if four arguments are provided.
# 2. Use default arguments in Python to achieve this functionality since Python does not natively support method overloading by function signatures.
# Write a Python program that:
# 1. Creates an instance of the Calculator class.
# 2. Demonstrates calling the add() method with two, three, and four arguments.

class Calculator:
    def add(self, a, b, c=0, d=0):
        return a + b + c + d


calc = Calculator()

print("Addition of 2 numbers:", calc.add(10, 20))
print("Addition of 3 numbers:", calc.add(10, 20, 30))
print("Addition of 4 numbers:", calc.add(10, 20, 30, 40))
