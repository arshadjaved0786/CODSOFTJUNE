# 🚀 Advanced Python Calculator (Beginner Friendly)

import math  # For square root function

def show_menu():
    print("\n===== ADVANCED CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Modulus (x % y)")
    print("7. Square Root")
    print("8. Exit")

# ➕ Addition
def add(a, b):
    return a + b

# ➖ Subtraction
def subtract(a, b):
    return a - b

# ✖ Multiplication
def multiply(a, b):
    return a * b

# ➗ Division
def divide(a, b):
    if b == 0:
        return "❌ Error: Cannot divide by zero!"
    return a / b

# 𝑥ʸ Power
def power(a, b):
    return a ** b

# % Modulus
def modulus(a, b):
    return a % b

# √ Square Root
def square_root(a):
    if a < 0:
        return "❌ Error: Cannot find square root of negative number!"
    return math.sqrt(a)

# 🧮 Main Calculator Logic
def calculator():
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '8':
            print("✅ Exiting calculator. Thanks for using!")
            break

        # Square root needs only one number
        if choice == '7':
            try:
                num = float(input("Enter a number: "))
                print("✅ Result:", square_root(num))
            except:
                print("❌ Please enter a valid number.")
        elif choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("✅ Result:", add(num1, num2))
                elif choice == '2':
                    print("✅ Result:", subtract(num1, num2))
                elif choice == '3':
                    print("✅ Result:", multiply(num1, num2))
                elif choice == '4':
                    print("✅ Result:", divide(num1, num2))
                elif choice == '5':
                    print("✅ Result:", power(num1, num2))
                elif choice == '6':
                    print("✅ Result:", modulus(num1, num2))
            except:
                print("❌ Invalid input. Please enter numbers only.")
        else:
            print("❌ Invalid choice. Enter a number between 1 and 8.")

# ▶ Run the calculator
calculator()
