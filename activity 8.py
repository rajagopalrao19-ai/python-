
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
prepared = [100, 120, 150, 100, 130]
served = [90, 100, 120, 95, 100]
waste_limit = 15
print("--- Food Waste Monitoring Report ---")
for i in range(len(days)):
    leftovers = prepared[i] - served[i]
    wastage = (leftovers / prepared[i]) * 100
    print("\nDay:", days[i])
    print("Meals Prepared:", prepared[i])
    print("Meals Served:", served[i])
    print("Leftover Meals:", leftovers)
    print("Wastage Percentage:", round(wastage, 2), "%")
    if wastage > waste_limit:
        print("Status: Excessive Food Waste")
    else:
        print("Status: Acceptable Food Waste")
print("\nMonitoring Completed.")
