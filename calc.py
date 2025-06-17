# Project Title: Simple Calculator
# Author: [Himani Tyagi]
# Internship Project Submission
# Description: This is a basic calculator that performs addition, subtraction, multiplication, and division.

import time

def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract second number from first"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide first number by second"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("===== Simple Calculator =====")
    print("You can choose from:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    time.sleep(0.5)

    choice = input("Enter choice (1/2/3/4 or +, -, *, /): ").strip()

    if choice in ['1', '2', '3', '4', '+', '-', '*', '/']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
            return

        if choice in ['1', '+']:
            result = add(num1, num2)
            op = '+'
        elif choice in ['2', '-']:
            result = subtract(num1, num2)
            op = '-'
        elif choice in ['3', '*']:
            result = multiply(num1, num2)
            op = '*'
        elif choice in ['4', '/']:
            result = divide(num1, num2)
            op = '/'

        print(f"\nResult: {num1} {op} {num2} = {result}\n")
    else:
        print("Invalid choice. Please select a valid operation.\n")

# === Main Loop ===
while True:
    calculator()
    time.sleep(0.5)
    cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if cont != 'yes':
        print("Thanks for using the calculator. Goodbye! 👋")
        break
