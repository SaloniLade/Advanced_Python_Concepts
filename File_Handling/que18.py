# Store employee ID, name, department, and salary in a file. 
# Write functions to:  
# • Display all employees.
# • Find the highest-paid employee.  
# • Calculate average salary.  
# • Display employees earning above a given salary.
with open("employees.txt", "w") as file:
    file.write("101,Amit,IT,50000\n")
    file.write("102,Priya,HR,60000\n")
    file.write("103,Rahul,Sales,45000\n")

def read_employees():
    employees = []
    with open("employees.txt", "r") as file:
        for line in file:
            emp_id, name, dept, salary = line.strip().split(",")
            employees.append(
                (emp_id, name, dept, float(salary))
            )
    return employees

def display_employees():
    for emp in read_employees():
        print(emp)

def highest_paid():
    employees = read_employees()
    return max(employees, key=lambda e: e[3])

def average_salary():
    employees = read_employees()
    return sum(e[3] for e in employees) / len(employees)

def above_salary(amount):
    for emp in read_employees():
        if emp[3] > amount:
            print(emp)

print("All Employees:")
display_employees()

print("\nHighest-Paid Employee:")
print(highest_paid())

print("\nAverage Salary:", average_salary())

print("\nEmployees earning above 50000:")
above_salary(50000)