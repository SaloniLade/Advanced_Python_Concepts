# Electricity bill using modular functions
# Assumed rates: first 100 units ₹5/unit, next 100 units ₹7/unit, and remaining units ₹10/unit. Fixed charge ₹50, tax 5%, and discount 10% for bills above ₹2,000. These are example rates.
def calculate_units(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    else:
        return 500 + 700 + (units - 200) * 10

def calculate_bill(units):
    energy = calculate_units(units)
    fixed = 50
    subtotal = energy + fixed
    tax = subtotal * 0.05
    total = subtotal + tax

    if total > 2000:
        total = total - total * 0.10

    return total

units = int(input("Enter units consumed: "))
print("Final bill = Rs.", calculate_bill(units))