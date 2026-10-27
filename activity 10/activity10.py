
products = {
    "Laptop": {"price": 50000, "stock": 10},
    "Phone": {"price": 20000, "stock": 15},
    "Headphones": {"price": 2000, "stock": 20}
}

total_revenue = 0
total_returns = 0

orders = [
    {"product": "Laptop", "qty": 2, "discount": 10, "returned": 0},
    {"product": "Phone", "qty": 3, "discount": 5, "returned": 1},
    {"product": "Headphones", "qty": 4, "discount": 0, "returned": 1}
]

print("E-COMMERCE ORDER REPORT")

for i, order in enumerate(orders, start=1):
    name = order["product"]
    qty = order["qty"]
    discount = order["discount"]
    returned = order["returned"]

    price = products[name]["price"]

    if qty > products[name]["stock"]:
        print(name, "- Insufficient stock")
        continue
    amount = price * qty
    discount_amount = amount * discount / 100
    net_amount = amount - discount_amount
    products[name]["stock"] -= qty
    if returned > qty:
        returned = 0
        print("Invalid return quantity for", name)

    products[name]["stock"] += returned

    refund = (net_amount / qty) * returned
    revenue = net_amount - refund

    total_revenue += revenue
    total_returns += refund

    print("\nOrder", i, ":", name)
    print("Quantity Dispatched:", qty)
    print("Discount:", discount, "%")
    print("Returned Quantity:", returned)
    print("Refund Amount: Rs.", round(refund, 2))
    print("Order Revenue: Rs.", round(revenue, 2))

    expected_stock = 10 if name == "Laptop" else (
        15 if name == "Phone" else 20
    )

    print("Stock Updated:", products[name]["stock"])

print("\n--- FINAL RECONCILIATION ---")
print("Total Revenue: Rs.", round(total_revenue, 2))
print("Total Refunds: Rs.", round(total_returns, 2))

print("\n--- FINAL INVENTORY SUMMARY ---")
for name, details in products.items():
    print(name, ":", details["stock"], "units remaining")

print("\n--- DISCREPANCY CHECK ---")
for name, details in products.items():
    if details["stock"] < 0:
        print("Discrepancy in", name)
    else:
        print(name, "- Stock is valid")
