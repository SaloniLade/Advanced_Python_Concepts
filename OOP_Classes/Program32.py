# Write python program to demonstrate multilevel inheritance. You need to define three classes:
# 1. Person: This class will represent a person with basic attributes like name and age.
# 2. Employee: This class will inherit from Person and add additional attributes related to an employee, such as employee ID and salary.
# 3. Manager: This class will inherit from Employee and add additional functionality related to a manager, such as department and team size.
# Class Details:

# 1. Person class should have the following attributes:
# - name: The name of the person.
# - age: The age of the person.
#    Method:

# - display_person_info(): Displays the person's name and age.

# 2. Employee class should inherit from Person and add the following attributes:
# - employee_id: The unique employee ID.
# - salary: The salary of the employee.
#    Method:

# - display_employee_info(): Displays the employee's ID and salary, as well as the name and age using the Person class's method.

# 3. Manager class should inherit from Employee and add the following attributes:
# - department: The department managed by the manager.
# - team_size: The size of the manager's team.
#    Method:

# - display_manager_info(): Displays the manager's department, team size, and all information related to the employee and the person.

# Write a Python program that:
# 1. Creates an instance of the Manager class.
# 2. Initializes all attributes for the manager, including inherited attributes.
# Calls the method to display all the personal, employee, and managerial details.

class Person:
    def __init__(self, name):
        self.name = name

    def show_person(self):
        print("Name:", self.name)


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def show_employee(self):
        self.show_person()
        print("Employee ID:", self.employee_id)


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def show_manager(self):
        self.show_employee()
        print("Department:", self.department)


manager = Manager("Sneha", 101, "IT")
manager.show_manager()
