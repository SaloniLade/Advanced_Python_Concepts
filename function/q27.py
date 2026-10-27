# Hospital billing system
def consultation():
    return 500

def laboratory():
    return 800

def medicine():
    return 400

def room():
    return 1000

def final_bill(category):
    total = consultation() + laboratory() + medicine() + room()

    if category == "senior":
        total = total * 0.80
    elif category == "regular":
        total = total * 0.95

    return total

category = input("Enter category (senior/regular/other): ").lower()
print("Final hospital bill = Rs.", final_bill(category))