# Asking the user how many numbers they want to enter
total_numbers = int(input("How many numbers? "))

# Initializing variables
sum_of_numbers = 0
maximum_number = None
minimum_number = None

# Loop to take input multiple times
for count in range(1, total_numbers + 1):

    current_number = float(input(f"Enter number {count}: "))

    # Adding number to sum
    sum_of_numbers += current_number

    # Setting first number as initial max and min
    if maximum_number is None or current_number > maximum_number:
        maximum_number = current_number

    if minimum_number is None or current_number < minimum_number:
        minimum_number = current_number

# Calculating average
average = sum_of_numbers / total_numbers

# Displaying results
print("\n----- RESULTS -----")
print("Sum:", sum_of_numbers)
print("Average:", average)
print("Maximum:", maximum_number)
print("Minimum:", minimum_number)
