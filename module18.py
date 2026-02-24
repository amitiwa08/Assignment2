def add(a, b):
    return a + b


# Function to subtract two numbers
def subtract(a, b):
    return a - b


# Function to multiply two numbers
def multiply(a, b):
    return a * b


# Function to divide two numbers (handles division by zero)
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Function to calculate modulus
def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b


# Function to calculate power
def power(a, b):
    return a ** b


# Main calculator function
def calculator():

    while True:
        print("\n===== FUNCTION CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Exiting calculator... Goodbye!")
            break

        # Taking numbers from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Calling appropriate function
        if choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

        elif choice == "3":
            result = multiply(num1, num2)

        elif choice == "4":
            result = divide(num1, num2)

        elif choice == "5":
            result = modulus(num1, num2)

        elif choice == "6":
            result = power(num1, num2)

        else:
            print("Invalid choice! Please select between 1 and 7.")
            continue

        print("Result:", result)


# Calling the main function
calculator()
