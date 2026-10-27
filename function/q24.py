# Banking system using functions
balance = 1000
history = []

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        history.append("Deposited: " + str(amount))
        print("Deposit successful")
    else:
        print("Invalid amount")

def withdrawal(amount):
    global balance
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        history.append("Withdrawn: " + str(amount))
        print("Withdrawal successful")

def balance_enquiry():
    print("Balance =", balance)

def transaction_history():
    for item in history:
        print(item)

deposit(500)
withdrawal(200)
balance_enquiry()
transaction_history()