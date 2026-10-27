
inventory = [
    ("Ethanol", "Flammable", 10),
    ("Acid", "Acid", 5),
    ("Bleach", "Oxidizer", 8),
    ("Petrol", "Flammable", 25)
]

max_quantity = {
    "Flammable": 30,
    "Acid": 10,
    "Oxidizer": 15
}

incompatible = [
    ("Acid", "Oxidizer"),
    ("Flammable", "Oxidizer")
]

invalid = False

print("--- Chemical Inventory Validation ---")

for name, category, quantity in inventory:
    if category not in max_quantity:
        print(name, "- Invalid storage category")
        invalid = True
    elif quantity > max_quantity[category]:
        print(name, "- Quantity exceeds maximum limit")
        invalid = True

for i in range(len(inventory)):
    name1, cat1, qty1 = inventory[i]

    for j in range(i + 1, len(inventory)):
        name2, cat2, qty2 = inventory[j]

        if ((cat1, cat2) in incompatible or
            (cat2, cat1) in incompatible):
            print("Incompatible combination:", name1, "and", name2)
            invalid = True
if invalid:
    print("\nInventory contains invalid records.")
else:
    print("\nInventory validation successful.")
