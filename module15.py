number = int(input("Enter a number: "))

# Handling negative numbers, 0 and 1
if number < 2:
    print(f"{number} is NOT a prime number.")
    print("Reason: Prime numbers are greater than 1.")

# Special case for 2 (smallest prime number)
elif number == 2:
    print("2 is a PRIME number.")
    print("Reason: 2 is the smallest and only even prime number.")

else:
    is_prime = True  # Assuming number is prime initially

    # Checking divisibility from 2 to square root of number
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a PRIME number.")
    else:
        print(f"{number} is NOT a prime number.")


# ---------------- PART 2 ----------------
# Finding prime numbers in a given range

start_range = int(input("\nEnter start range: "))
end_range = int(input("Enter end range: "))

print("\nPrime numbers:", end=" ")

for current_number in range(start_range, end_range + 1):

    if current_number < 2:
        continue  # Skip numbers less than 2

    is_prime = True

    for divisor in range(2, int(current_number ** 0.5) + 1):
        if current_number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(current_number, end=", ")

print()
