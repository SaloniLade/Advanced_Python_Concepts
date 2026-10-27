# Write a Python program that:
# - Creates two BankAccount objects for two different account holders.
# - Demonstrates the functionality of the methods by performing some deposits, withdrawals, and transfers between the accounts.
# The class should have the following attributes and methods:

# Attributes:
# - account_holder: The name of the person who owns the account.
# - balance: The current balance in the account (initial balance should be 0).
# - account_number: A unique number for the account (you can generate this automatically by keeping track of a class-level counter).
# Methods:
# 1. deposit(amount): Adds the specified amount to the account balance.
# 2. withdraw(amount): Subtracts the specified amount from the balance, but only if the account has sufficient funds. Otherwise, print an error message.
# 3. display_balance(): Prints the current account balance.
# 4. transfer(amount, other_account): Transfers the specified amount from this account to another account, if sufficient balance is available. Otherwise, print an error message.

class BankAccount:
    next_account_number = 1001

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def transfer(self, other, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            other.balance += amount
            print("Transfer successful.")

    def display(self):
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


account1 = BankAccount("Amit", 5000)
account2 = BankAccount("Priya", 2000)

account1.deposit(1000)
account1.withdraw(500)
account1.transfer(account2, 1000)

print("\nAccount 1:")
account1.display()

print("\nAccount 2:")
account2.display()
