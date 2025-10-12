# Author: Alejandro Ceballos
# Date: 2025-10-12

# Assignment 1: Creating Python Programs
# Part 1:
# Write a Python program to find the addition and subtraction of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, add them together to find the output. Also, subtract the two numbers to find the output.

# Part 2:
# Write a Python program to find the multiplication and division of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, multiply them together to find the output. Also, divide num1/num2 to find the output.

# // Part 1: Addition and Subtraction //

# Get user input
print("// Part 1 Addition and Subtraction //")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# add both numbers
addition = num1 + num2
# subtract both numbers
subtraction = num1 - num2

# Display results to the user
print(f"The addition of {num1} and {num2} is: {addition}")
print(f"The subtraction of {num1} and {num2} is: {subtraction}", end="\n\n")

# // Part 2: Multiplication and Division //

# Get user input
print("// Part 2 Multiplication and Division //")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# multiply both numbers
multiplication = num1 * num2

# Display results to the user
print(f"The multiplication of {num1} and {num2} is: {multiplication}")

# Perform division with error handling for division by zero
if num2 != 0:
    division = num1 / num2
    print(f"The division of {num1} by {num2} is: {division}")
else:
    print("Error: Cannot divide a number by zero.")