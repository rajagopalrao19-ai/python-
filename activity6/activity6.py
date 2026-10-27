
appliances = ["Fan", "Light", "TV"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
readings = [
    [2, 2, 3, 2, 3, 4, 3],
    [1, 1, 1, 2, 1, 2, 2],
    [3, 3, 4, 3, 4, 5, 4]
]
limit = 10
print("--- Weekly Electricity Consumption ---")
for i in range(len(appliances)):
    total = sum(readings[i])
    print(appliances[i], "total:", total, "kWh")
    if total > limit:
        print("Warning: Consumption exceeds limit!")
print("\nDaily Consumption:")
for j in range(len(days)):
    daily_total = 0
    for i in range(len(appliances)):
        daily_total += readings[i][j]
    print(days[j], ":", daily_total, "kWh")
grand_total = sum(sum(row) for row in readings)

print("\nWeekly Total:", grand_total, "kWh")
