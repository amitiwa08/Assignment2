# Setting initial account balance
account_balance = 10000

# Minimum balance rule
minimum_balance = 500

# Running the ATM system continuously until user exits
while True:

    print("\n===== ATM SIMULATOR =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    # Taking user choice
    user_choice = int(input("Enter your choice: "))

    # Option 1: Check Balance
    if user_choice == 1:
        print(f"Your current balance is: ₹{account_balance:.2f}")

    # Option 2: Deposit Money
    elif user_choice == 2:
        deposit_amount = float(input("Enter amount to deposit: ₹"))

        if deposit_amount > 0:
            account_balance += deposit_amount
            print("Deposit successful!")
            print(f"Updated balance: ₹{account_balance:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    # Option 3: Withdraw Money
    elif user_choice == 3:
        withdraw_amount = float(input("Enter amount to withdraw: ₹"))

        # Checking if withdrawal keeps minimum balance
        if withdraw_amount <= 0:
            print("Withdrawal amount must be greater than zero.")

        elif withdraw_amount > account_balance:
            print("Insufficient balance!")

        elif account_balance - withdraw_amount < minimum_balance:
            print("Cannot withdraw! Minimum balance of ₹500 must remain.")

        else:
            account_balance -= withdraw_amount
            print("Withdrawal successful!")
            print(f"New balance: ₹{account_balance:.2f}")

    # Option 4: Exit
    elif user_choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    # Invalid choice handling
    else:
        print("Invalid choice! Please select between 1 and 4.")
