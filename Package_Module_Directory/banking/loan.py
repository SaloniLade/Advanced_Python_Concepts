
def calculate_simple_interest(principal, rate, years):
    return principal * rate * years / 100

def calculate_loan_amount(principal, rate, years):
    interest = calculate_simple_interest(
        principal, rate, years
    )
    return principal + interest
