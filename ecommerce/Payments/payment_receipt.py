
def generate_receipt(customer, amount, success):
    print("\n--- Payment Receipt ---")
    print("Customer:", customer["name"])
    print("Customer ID:", customer["customer_id"])
    print("Amount: Rs.", amount)
    print("Payment Status:", "Successful" if success else "Failed")
