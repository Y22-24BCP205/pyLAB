import math

def print_alphabets():
    print("Uppercase Alphabets:")
    for i in range(65, 91):  # ASCII values for A-Z
        print(chr(i), end=' ')
    print("\nLowercase Alphabets:")
    for i in range(97, 123):  # ASCII values for a-z
        print(chr(i), end=' ')
    print()

def multiplication_table(n):
    print(f"Multiplication Table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def count_alphabets_and_digits(s):
    alphabets = sum(c.isalpha() for c in s)
    digits = sum(c.isdigit() for c in s)
    return alphabets, digits

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

def generate_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer() and c <= limit:
                triplets.append((a, b, int(c)))
    return triplets

def print_24_hour_format():
    for hour in range(24):
        if hour == 0:
            print("12:00 AM")
        elif hour == 12:
            print("12:00 PM")
        elif hour < 12:
            print(f"{hour}:00 AM")
        else:
            print(f"{hour - 12}:00 PM")

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def nPr(n, r):
    return factorial(n) // factorial(n - r)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def print_n_natural_numbers_reverse(n):
    for i in range(n, 0, -1):
        print(i, end=' ')
    print()

def generate_fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

def calculate_sin(x):
    sin_x = 0
    for n in range(10):  # Using 10 terms for approximation
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        sin_x += term
    return sin_x

def main():
    print("Select an operation:")
    print("1. Print all alphabets in upper case and in lower case")
    print("2. Print a multiplication table of a given number")
    print("3. Count number of alphabets and number of digits in a string")
    print("4. Check various properties of a given number")
    print("5. Generate all Pythagorean Triplets with side length <= 30")
    print("6. Print 24 hours of day with suitable suffixes")
    print("7. Print nCr and nPr")
    print("8. Print factorial of a given number")
    print("9. Print N natural numbers in reverse")
    print("10. Generate N numbers of Fibonacci series")
    print("11. Calculate sin(x) for a radian value")

    choice = int(input("Enter your choice (1-11): "))

    if choice == 1:
        print_alphabets()
    elif choice == 2:
        number = int(input("Enter a number: "))
        multiplication_table(number)
    elif choice == 3:
        user_string = input("Enter a string: ")
        alphabets, digits = count_alphabets_and_digits(user_string)
        print("Number of alphabets:", alphabets)
        print("Number of digits:", digits)
    elif choice == 4:
        number = int(input("Enter a number: "))
        print("Is prime:", is_prime(number))
        print("Is perfect:", is_perfect(number))
        print("Is Armstrong:", is_armstrong(number))
        print("Is palindrome:", is_palindrome(number))
        print("Is automorphic:", is_automorphic(number))
    elif choice == 5:
        triplets = generate_pythagorean_triplets(30)
        print("Pythagorean Triplets with side length <= 30:")
        for triplet in triplets:
            print(triplet)
    elif choice == 6:
        print_24_hour_format()
    elif choice == 7:
        n = int(input("Enter n: "))
        r = int(input("Enter r: "))
        print("nCr:", nCr(n, r))
        print("nPr:", nPr(n, r))
    elif choice == 8:
        number = int(input("Enter a number: "))
        print("Factorial:", factorial(number))
    elif choice == 9:
        n = int(input("Enter N: "))
        print_n_natural_numbers_reverse(n)
    elif choice == 10:
        n = int(input("Enter N: "))
        fib_series = generate_fibonacci(n)
        print("Fibonacci series:", fib_series)
    elif choice == 11:
        x = float(input("Enter x in radians: "))
        print("sin(x):", calculate_sin(x))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
