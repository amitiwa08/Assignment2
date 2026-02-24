year = int(input("Enter a year: "))

# Checking leap year conditions
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):

    print("\nYear:", year)
    print("Result: Leap Year")

    # Explaining why clearly
    if year % 400 == 0:
        print("Reason: The year is divisible by 400.")
    elif year % 100 != 0:
        print("Reason: The year is divisible by 4 and not divisible by 100.")

else:

    print("\nYear:", year)
    print("Result: NOT a Leap Year")

    # Explaining why clearly
    if year % 4 != 0:
        print("Reason: The year is not divisible by 4.")
    elif year % 100 == 0 and year % 400 != 0:
        print("Reason: The year is divisible by 100 but not divisible by 400.")
