
# Asking the user to enter a number
number = int(input("Enter a number: "))

# Handling negative numbers
if number < 0:
    print("Factorial is not defined for negative numbers.")

# Handling 0 separately
elif number == 0:
    print("0! = 1")
    print("Reason: Factorial of 0 is defined as 1.")

else:
    factorial = 1
    steps = ""   # To store step-by-step multiplication

    # Loop from number down to 1
    for current in range(number, 0, -1):
        factorial *= current

        # Building the step string
        steps += str(current)
        if current != 1:
            steps += " × "

    # Displaying final result
    print(f"{number}! = {steps} = {factorial}")
