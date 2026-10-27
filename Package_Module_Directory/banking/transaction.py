
def deposit(account, amount):
    if amount <= 0:
        return "Amount must be positive"
    account["balance"] += amount
    return "Deposit successful"

def withdraw(account, amount):
    if amount <= 0:
        return "Amount must be positive"
    if amount > account["balance"]:
        return "Insufficient balance"

    account["balance"] -= amount
    return "Withdrawal successful"
