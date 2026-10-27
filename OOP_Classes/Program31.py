# Write a Python program that:
# 1. Creates an instance of the Employee class.
# 2. Initializes all attributes for the employee, including inherited attributes.
# 3. Calls the method to display both personal and employee-specific details.
# Create two classes:
# 1. Person: This class will represent a person with basic details like name and age.
# 2. Employee: This class will inherit from the Person class and add additional functionality related to an employee, such as employee ID and salary.
# Class Details:

# - Person class should have the following attributes:
# - name: The name of the person.
# - age: The age of the person.
#   It should also have a method:

# - display_person_info(): Displays the name and age of the person.

# - Employee class should inherit from the Person class and add the following attributes:
# - employee_id: A unique identifier for the employee.
# - salary: The salary of the employee.
#   It should also have a method:

# - display_employee_info(): Displays the employee's ID, salary, name, and age (make use of the parent class method to display the name and age).

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        self.display_person()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


emp = Employee("Rahul", 25, 101, 30000)
emp.display_employee()
