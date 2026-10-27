# 13. Create a directory named ecommerce containing packages for: 
# a) Products  b) Customers  c) Orders  d) Payments 
#  Each package should contain at least two modules. 

from Products.product_details import get_products
from Products.product_search import search_product
from Customers.customer_details import get_customer
from Customers.customer_validation import validate_customer
from Orders.order_create import create_order
from Orders.order_summary import display_order
from Payments.payment_process import process_payment
from Payments.payment_receipt import generate_receipt

name = input("Enter customer name: ")
customer_id = input("Enter customer ID: ")

if not validate_customer(name, customer_id):
    print("Invalid customer details.")
else:
    customer = get_customer(name, customer_id)
    products = get_products()

    print("\n--- Available Products ---")
    for p in products:
        print(p["name"], "- Rs.", p["price"])

    product_name = input("\nEnter product name: ")
    product = search_product(products, product_name)

    if product is None:
        print("Product not found.")
    else:
        quantity = int(input("Enter quantity: "))
        order = create_order(product, quantity)

        if order is None:
            print("Invalid quantity.")
        else:
            display_order(order)
            success = process_payment(order["total"])
            generate_receipt(customer, order["total"], success)
