# Product invoice with GST and coupon discount
def subtotal(prices, quantities):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * quantities[i]
    return total

def invoice(prices, quantities, discount, gst):
    total = subtotal(prices, quantities)
    total = total - total * discount / 100
    total = total + total * gst / 100
    return total

prices = list(map(float, input("Enter prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))

if len(prices) != len(quantities):
    print("Prices and quantities must have equal lengths.")
else:
    d = float(input("Enter coupon discount (%): "))
    g = float(input("Enter GST (%): "))
    print("Final invoice = Rs.", invoice(prices, quantities, d, g))