# Author: Alejandro Ceballos
# Date: 2025-11-09
# Module 5: Critical Thinking Assignment

# // Part 1: Rainfall Program //
print("// Rainfall Program //")
years = int(input("Number of years: "))
rainfall = 0
months = years * 12

for year in range(1, years + 1):
    print(f"Current Year - {year}")
    
    for month in range(1, 13):
        rainfall_per_month = float(input(f"Inches of rain for month {month}: "))
        rainfall += rainfall_per_month
        
avg_rainfall = rainfall / months

print("\n")
print(f"Total months: {months}")
print(f"Total inches of rainfall: {rainfall:.2f}")
print(f"Average rainfall for each month: {avg_rainfall:.2f} inches\n")

# // Part 2: Book Point Program //
print("// Book Point Program //")
num_purchased = int(input("How many books have you purchased this month?: "))

if num_purchased == 0:
    points = 0
elif num_purchased >= 2:
    points = 5
elif num_purchased >= 4:
    points = 15
elif num_purchased >= 6:
    points = 30
elif num_purchased >= 8:
    points = 60
else:
    points = 0
    
print(f"You've earned a total of {points} points this month!")