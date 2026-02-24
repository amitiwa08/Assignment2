try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    addition = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number
    exponentiation = first_number ** second_number

    if second_number != 0:
        division = first_number / second_number
        modulus = first_number % second_number
    else:
        division = "Undefined (Cannot divide by zero)"
        modulus = "Undefined (Cannot divide by zero)"

    print("\n----- CALCULATION RESULTS -----")
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)
    print("Modulus:", modulus)
    print("Exponentiation:", exponentiation)

except ValueError:
    print("Invalid input! Please enter numeric values only.")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

except Exception as error:
    print("Something went wrong:", error)
