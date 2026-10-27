# Calculate an electricity bill based on units consumed.
# Assumption: Slabs are ₹5 per unit for the first 100 units, ₹7 for the next 100, and ₹10 per unit above 200. These are example rates, not official electricity tariffs.
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    return bill

units = int(input("Enter units consumed: "))
print("Electricity bill = Rs.", electricity_bill(units))