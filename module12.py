number = int(input("Enter number: "))

# Asking the user for the range limit
range_end = int(input("Enter range (end): "))

print(f"\nMultiplication Table of {number}\n")

# Looping from 1 to the given range
for multiplier in range(1, range_end + 1):

    # Calculating product
    product = number * multiplier

    # Displaying formatted result
    print(f"{number} x {multiplier} = {product}")
