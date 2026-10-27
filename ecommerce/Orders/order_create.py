
def create_order(product, quantity):
    if quantity <= 0:
        return None

    return {
        "product": product["name"],
        "quantity": quantity,
        "total": product["price"] * quantity
    }
