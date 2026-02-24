# Asking the user to enter a year
year = int(input("Enter a year: "))

# Checking leap year conditions based on given rules
# Rule:
# 1. Year must be divisible by 4
# 2. AND (not divisible by 100 OR divisible by 400)

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):

    # If condition is True → It is a leap year
    print("\nYear:", year)
    print("Result: Leap Year")

    # Explaining why
    if year % 400 == 0:
        print("Reason: The year is divisible by 400, so it is a leap year.")
    elif year % 100 == 0:
        print("Reason: The year is divisible by 100 but NOT by 400, so it is NOT a leap year.")
    else:
        print("Reason: The year is divisible by 4 and not divisible by 100.")

else:

    # If condition is False → Not a leap year
    print("\nYear:", year)
    print("Result: NOT a Leap Year")

    # Explaining why
    if year % 4 != 0:
        print("Reason: The year is not divisible by 4.")
    elif year % 100 == 0 and year % 400 != 0:
        print("Reason: The year is divisible by 100 but not divisible by 400.")
    else:
        print("Reason: The year does not satisfy leap year conditions.")
