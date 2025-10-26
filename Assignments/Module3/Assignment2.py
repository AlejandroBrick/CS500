# Author: Alejandro Ceballos
# Date: 2025-10-25

# Module 3: Critical Thinking Assignment 2
# Part 1: Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax. 
# Display each of these amounts and the total price.

# Part 2: Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.

# // Part 1: Meal Total Calculation //
print("// Part 1: Meal Total Calculation //")

meal_charge = float(input("Enter the price for the meal: "))

# Calculate tip, tax, and then total price
tip = meal_charge * 0.18
tax = meal_charge * 0.07
total_price = meal_charge + tip + tax

# Display totals
print(f"Total Tip(18%): {tip:.2f}")
print(f"Total Tax(7%): {tax:.2f}")
print(f"Total Price: {total_price:.2f}", end="\n\n")

# // Part 2: Alarm Time Calculation //
print("// Part 2: Alarm Time Calculation //")

# get our inputs
current_time = int(input("Enter your current time (0-23 hours): "))
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

# add wait time to current time then do a modulo 24 to adjust for 24hr format
alarm_time = (current_time + wait_hours) % 24

print("The alarm will sound at hour:", alarm_time)
