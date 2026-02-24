
user_input = input("Enter word/number: ")

# Storing original input
original_value = user_input

# Converting to lowercase for case-insensitive comparison
processed_value = user_input.lower()

# Reversing the processed value step-by-step using slicing
reversed_value = processed_value[::-1]

# Displaying step-by-step details
print("\n----- VERIFICATION -----")
print("Original:", original_value)
print("Reversed:", reversed_value)

# Checking if original (lowercase) equals reversed
if processed_value == reversed_value:
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")
