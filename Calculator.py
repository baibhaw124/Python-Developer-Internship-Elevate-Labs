# Calculator CLI App - Task 1
# Elevate Labs Python Internship
# Author: Baibhaw Kumar Upadhyay

import os
from datetime import datetime

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division with zero check
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# List to store calculation history
history = []

print("---- Simple Calculator ----")

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View History")
    print("6. Clear Screen")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    # Exit confirmation
    if choice == '7':
        confirm = input("Are you sure you want to exit? (yes/no): ").lower()
        if confirm == 'yes':
            print("Exiting calculator. Thank you!")
            break
        else:
            continue

    # View History
    if choice == '5':
        if not history:
            print("No history available yet.")
        else:
            print("\n----- Calculation History -----")
            for record in history:
                print(record)
        continue

    # Clear screen option
    if choice == '6':
        clear_screen()
        continue

  # Taking inputs in Form numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    # Performing operation based on choice
       # Perform operations based on user choice
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if choice == '1':
        result = add(num1, num2)
        print(f"Sum of {num1} + {num2} is:", result)
        history.append(f"[{timestamp}] {num1} + {num2} = {result}")

    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Subtraction of {num1} - {num2} is:", result)
        history.append(f"[{timestamp}] {num1} - {num2} = {result}")

    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Multiplication {num1} x {num2} is:", result)
        history.append(f"[{timestamp}] {num1} * {num2} = {result}")

    elif choice == '4':
        result = divide(num1, num2)
        print(f"Division of {num1} / {num2} is:", result)
        history.append(f"[{timestamp}] {num1} / {num2} = {result}")

    else:
        print("Invalid choice! Please try again.")