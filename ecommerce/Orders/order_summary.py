
def display_order(order):
    if order is None:
        print("Invalid order.")
        return

    print("Product:", order["product"])
    print("Quantity:", order["quantity"])
    print("Total Amount: Rs.", order["total"])
