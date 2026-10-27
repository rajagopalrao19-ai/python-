
product = input("Enter product name: ")
quantity = int(input("Enter quantity produced: "))
material_cost = float(input("Enter material cost per unit: "))
labour_cost = float(input("Enter labour cost per unit: "))
machine_cost = float(input("Enter machine cost per unit: "))
wastage_percent = float(input("Enter wastage percentage: "))
selling_price = float(input("Enter selling price per unit: "))
profit_target = float(input("Enter target profit: "))
materials = quantity * material_cost
labour = quantity * labour_cost
machine = quantity * machine_cost
wastage = materials * wastage_percent / 100
total_cost = materials + labour + machine + wastage
revenue = quantity * selling_price
profit = revenue - total_cost
print("\n--- Manufacturing Cost Report ---")
print("Product:", product)
print("Material Cost:", materials)
print("Labour Cost:", labour)
print("Machine Cost:", machine)
print("Wastage Cost:", round(wastage, 2))
print("Total Production Cost:", round(total_cost, 2))
print("Total Revenue:", round(revenue, 2))
print("Total Profit:", round(profit, 2))
if profit >= profit_target:
    print("Result: Profit target achieved!")
else:
    print("Result: Profit target not achieved.")
    print("Additional Profit Needed:",
          round(profit_target - profit, 2))
