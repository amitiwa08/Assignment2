
# 1. Factorial Function
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    if n == 0:
        return 1

    result = 1
    for number in range(1, n + 1):
        result *= number
    return result


# 2. Prime Check Function
def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


# 3. Fibonacci Function (nth Fibonacci number)
def fibonacci(n):
    if n < 0:
        return "Fibonacci not defined for negative numbers."
    if n == 0:
        return 0
    if n == 1:
        return 1

    first = 0
    second = 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second


# 4. Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


# 5. Reverse Number
def reverse_number(n):
    reversed_num = int(str(abs(n))[::-1])
    return -reversed_num if n < 0 else reversed_num


# 6. Armstrong Number Check
def is_armstrong(n):
    digits = str(abs(n))
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == abs(n)


# 7. GCD Function (Euclidean Algorithm)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


# 8. LCM Function
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


# 9. Perfect Number Check
def is_perfect_number(n):
    if n <= 1:
        return False

    divisor_sum = 0
    for divisor in range(1, n):
        if n % divisor == 0:
            divisor_sum += divisor

    return divisor_sum == n


# 10. Menu Function
def math_menu():

    while True:
        print("\n===== NUMBER SYSTEM MENU =====")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            n = int(input("Enter number: "))
            print("Result:", factorial(n))

        elif choice == "2":
            n = int(input("Enter number: "))
            print("Prime:", is_prime(n))

        elif choice == "3":
            n = int(input("Enter position (n): "))
            print("Fibonacci:", fibonacci(n))

        elif choice == "4":
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == "5":
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))

        elif choice == "6":
            n = int(input("Enter number: "))
            print("Armstrong:", is_armstrong(n))

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            n = int(input("Enter number: "))
            print("Perfect Number:", is_perfect_number(n))

        elif choice == "10":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1 and 10.")


# Calling the menu
math_menu()
