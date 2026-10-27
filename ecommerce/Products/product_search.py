
def search_product(products, name):
    for product in products:
        if product["name"].lower() == name.lower():
            return product
    return None
