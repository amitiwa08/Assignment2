while True:

    # Displaying menu options
    print("\n===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    # Taking user choice
    choice = int(input("Enter your choice (1-7): "))

    # Exit condition
    if choice == 7:
        print("Exiting program... Goodbye!")
        break

    # Asking for temperature value
    temperature = float(input("Enter temperature value: "))

    # Performing conversions based on user choice

    if choice == 1:
        # Celsius to Fahrenheit
        result = (temperature * 9/5) + 32
        print(f"Result: {result:.2f} °F")

    elif choice == 2:
        # Fahrenheit to Celsius
        result = (temperature - 32) * 5/9
        print(f"Result: {result:.2f} °C")

    elif choice == 3:
        # Celsius to Kelvin
        result = temperature + 273.15
        print(f"Result: {result:.2f} K")

    elif choice == 4:
        # Kelvin to Celsius
        result = temperature - 273.15
        print(f"Result: {result:.2f} °C")

    elif choice == 5:
        # Fahrenheit to Kelvin
        result = (temperature - 32) * 5/9 + 273.15
        print(f"Result: {result:.2f} K")

    elif choice == 6:
        # Kelvin to Fahrenheit
        result = (temperature - 273.15) * 9/5 + 32
        print(f"Result: {result:.2f} °F")

    else:
        print("Invalid choice! Please select between 1 and 7.")
