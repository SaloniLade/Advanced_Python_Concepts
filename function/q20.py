# Calculate gross salary after adding HRA and DA.
# Assumption: HRA is 20% and DA is 10% of basic salary.
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da
    return gross

basic = float(input("Enter basic salary: "))
print("Gross salary =", gross_salary(basic))