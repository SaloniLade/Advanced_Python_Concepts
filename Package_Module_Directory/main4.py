# Create a module containing functions to calculate gross salary, deductions, and net salary for an employee. 
import salary

basic = float(input("Enter basic salary: "))

gross = salary.gross_salary(basic)
deduction = salary.deductions(gross)
net = salary.net_salary(basic)

print("\n--- Employee Salary Slip ---")
print("Basic Salary:", basic)
print("Gross Salary:", round(gross, 2))
print("Deductions:", round(deduction, 2))
print("Net Salary:", round(net, 2))
