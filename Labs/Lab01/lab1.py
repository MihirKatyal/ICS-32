# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Mihir Katyal
# mkatyal@uci.edu
# 19099879

# Welcome message
print("Welcome to ICS 32 PyCalc!")

# Input from the user
operand1 = float(input("Enter your first operand: "))
operand2 = float(input("Enter your second operand: "))
operator = input("Enter your desired operator (+, -, or x): ")

def calculate(operand1, operand2, operator):
    """Performs a calculation based on two operands and an operator."""
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == 'x':
        return operand1 * operand2
    else:
        return "Invalid operator"

