# Calculate the total bill after applying a discount.
def total_bill(prices, quantities, discount):
    total = 0

    for i in range(len(prices)):
        total += prices[i] * quantities[i]

    final_bill = total - (total * discount / 100)
    return final_bill

prices = list(map(float, input("Enter item prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))
discount = float(input("Enter discount percentage: "))

if len(prices) == len(quantities):
    print("Final bill =", total_bill(prices, quantities, discount))
else:
    print("Prices and quantities must have equal lengths.")