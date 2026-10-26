
# Inventory Matrix Reconciliation

products = ["Laptop", "Mouse", "Keyboard"]
warehouses = ["Warehouse A", "Warehouse B", "Warehouse C"]

# Stock quantities in each warehouse
stock = [
    [50, 20, 30],   # Laptop
    [10, 40, 20],   # Mouse
    [30, 10, 15]    # Keyboard
]


target = [
    [30, 30, 40],
    [20, 25, 25],
    [20, 20, 15]
]
print("--- Inventory Reconciliation ---")
for i in range(len(products)):
    print("\nProduct:", products[i])
    surplus = []
    shortage = []
    for j in range(len(warehouses)):
        difference = stock[i][j] - target[i][j]
        if difference > 0:
            surplus.append([j, difference])
            print(warehouses[j], "Surplus:", difference)
        elif difference < 0:
            shortage.append([j, -difference])
            print(warehouses[j], "Shortage:", -difference)
    for s in surplus:
        for d in shortage:
            amount = min(s[1], d[1])
            if amount > 0:
                print("Transfer", amount, "units from",
                      warehouses[s[0]], "to",
                      warehouses[d[0]])
                s[1] -= amount
                d[1] -= amount
print("\nInventory reconciliation completed.")
