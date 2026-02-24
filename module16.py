import random   # Used to generate random number

best_score = None   # To track minimum attempts used

# Outer loop to allow replay
while True:

    print("\n===== NUMBER GUESSING GAME =====")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.\n")

    # Computer selects random number
    secret_number = random.randint(1, 100)

    attempts_remaining = 7
    attempts_used = 0
    guessed_correctly = False

    # Loop for 7 attempts
    while attempts_remaining > 0:

        guess = int(input("Enter your guess: "))
        attempts_used += 1
        attempts_remaining -= 1

        if guess == secret_number:
            print("\nCongratulations! You guessed it correctly!")
            print(f"You guessed the number in {attempts_used} attempts.")
            guessed_correctly = True

            # Updating best score
            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print(" New Best Score!")

            break

        elif guess > secret_number:
            print("Too high!")

        else:
            print("Too low!")

        # Bonus Hint: If guess is within 5
        if abs(guess - secret_number) <= 5 and guess != secret_number:
            print(" Very close!")

        print(f"Attempts remaining: {attempts_remaining}\n")

    # If user failed all attempts
    if not guessed_correctly:
        print("\n Game Over!")
        print(f"The correct number was: {secret_number}")

    # Display best score if available
    if best_score is not None:
        print(f" Best Score (minimum attempts): {best_score}")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing! Goodbye ")
        breakmodule16.py
