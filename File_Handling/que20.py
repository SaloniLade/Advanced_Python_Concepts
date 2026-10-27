# Store deposits and withdrawals in a file. 
# Read the file and calculate:  
# • Total deposits  
# • Total withdrawals 
# • Final balance  
# • Largest transaction 

with open("transactions.txt", "w") as file:
    file.write("Deposit,5000\n")
    file.write("Withdrawal,-1000\n")
    file.write("Deposit,3000\n")
    file.write("Withdrawal,-1500\n")

total_deposits = 0
total_withdrawals = 0
balance = 0
largest = 0

with open("transactions.txt", "r") as file:
    for line in file:
        transaction, amount = line.strip().split(",")
        amount = float(amount)

        if amount > 0:
            total_deposits += amount
        else:
            total_withdrawals += abs(amount)

        balance += amount

        if abs(amount) > largest:
            largest = abs(amount)

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", balance)
print("Largest Transaction:", largest)