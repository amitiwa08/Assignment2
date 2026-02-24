# Asking the user to choose a pattern
print("===== NUMBER PATTERN PRINTER =====")
print("1. Pattern 1")
print("2. Pattern 2")
print("3. Pattern 3")
print("4. Pattern 4")

pattern_choice = int(input("Enter pattern number (1-4): "))
height = int(input("Enter height of the pattern: "))

print("\n----- OUTPUT -----\n")

# ---------------- Pattern 1 ----------------
# 1
# 1 2
# 1 2 3
if pattern_choice == 1:

    for row in range(1, height + 1):
        for number in range(1, row + 1):
            print(number, end=" ")
        print()   # Move to next line


# ---------------- Pattern 2 ----------------
# 1
# 2 2
# 3 3 3
elif pattern_choice == 2:

    for row in range(1, height + 1):
        for count in range(row):
            print(row, end=" ")
        print()


# ---------------- Pattern 3 ----------------
# 5 4 3 2 1
# 4 3 2 1
elif pattern_choice == 3:

    for row in range(height, 0, -1):
        for number in range(row, 0, -1):
            print(number, end=" ")
        print()


# ---------------- Pattern 4 ----------------
# 1
# 121
# 12321
elif pattern_choice == 4:

    for row in range(1, height + 1):

        # Increasing part
        for number in range(1, row + 1):
            print(number, end="")

        # Decreasing part
        for number in range(row - 1, 0, -1):
            print(number, end="")

        print()


else:
    print("Invalid pattern choice! Please select between 1 and 4.")
