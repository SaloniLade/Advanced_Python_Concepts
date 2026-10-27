
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

def deductions(gross):
    return gross * 0.05

def net_salary(basic):
    gross = gross_salary(basic)
    deduction = deductions(gross)
    return gross - deduction
