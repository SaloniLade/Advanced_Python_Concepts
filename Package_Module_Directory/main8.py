# 9. Develop a package banking containing:
# a) account.py – account creation and balance 
# b) transaction.py – deposit and withdrawal  
# c) loan.py – loan calculation
# Create a main program to use the package. 
from banking.account import create_account, get_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_simple_interest, calculate_loan_amount

name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
balance = float(input("Enter opening balance: "))

if balance < 0:
    print("Opening balance cannot be negative.")
else:
    account = create_account(name, account_number, balance)

    print("\nAccount Created Successfully")
    print("Name:", account["name"])
    print("Account Number:", account["account_number"])
    print("Balance:", get_balance(account))

    amount = float(input("\nEnter deposit amount: "))
    print(deposit(account, amount))

    amount = float(input("Enter withdrawal amount: "))
    print(withdraw(account, amount))

    print("Final Balance:", get_balance(account))

    principal = float(input("\nEnter loan principal: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = float(input("Enter loan period in years: "))

    if principal < 0 or rate < 0 or years < 0:
        print("Loan values cannot be negative.")
    else:
        interest = calculate_simple_interest(
            principal, rate, years
        )
        total = calculate_loan_amount(principal, rate, years)

        print("Loan Interest:", round(interest, 2))
        print("Total Loan Amount:", round(total, 2))
