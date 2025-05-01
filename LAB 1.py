def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def add_multiply_subtract_divide(a, b):
    return {
        "addition": add(a, b),
        "subtraction": subtract(a, b),
        "multiplication": multiply(a, b),
        "division": divide(a, b)
    }

def hours_to_minutes(hours):
    return hours * 60

def minutes_to_hours(minutes):
    return minutes / 60

def dollars_to_rs(dollars):
    return dollars * 48

def rs_to_dollars(rs):
    return rs / 48

def dollars_to_pounds(dollars):
    return (dollars * 48) / 70

def grams_to_kg(grams):
    return grams / 1000

def kg_to_grams(kgs):
    return kgs * 1000

def bytes_to_units(bytes):
    return {
        "KB": bytes / 1024,
        "MB": bytes / (1024 ** 2),
        "GB": bytes / (1024 ** 3)
    }

def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

def calculate_interest(principal, rate, time):
    return (principal * rate * time) / 100

def square_area_perimeter(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    return {"area": area, "perimeter": perimeter}

def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return {"area": area, "perimeter": perimeter}

def circle_area(radius):
    return (22/7) * radius * radius

def triangle_area(base, height):
    return (base * height) / 2

def calculate_net_salary(gross_salary):
    allowance = 0.10 * gross_salary
    deduction = 0.03 * gross_salary
    net_salary = gross_salary + allowance - deduction
    return net_salary

def calculate_net_sales(gross_sales):
    discount = 0.10 * gross_sales
    net_sales = gross_sales - discount
    return net_sales

def average_of_subjects(subject1, subject2, subject3):
    total = subject1 + subject2 + subject3
    average = total / 3
    return {"total": total, "average": average}

def swap(a, b):
    return b, a

# Main function to demonstrate the usage of the above functions
def main():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Add, Multiply, Subtract, and Divide")
    print("6. Convert hours to minutes")
    print("7. Convert minutes to hours")
    print("8. Convert dollars to Rs.")
    print("9. Convert Rs. to dollars")
    print("10. Convert dollars to pounds")
    print("11. Convert grams to kg")
    print("12. Convert kg to grams")
    print("13. Convert bytes to KB, MB, GB")
    print("14. Convert Celsius to Fahrenheit")
    print("15. Convert Fahrenheit to Celsius")
    print("16. Calculate interest")
    print("17. Calculate area & perimeter of a square")
    print("18. Calculate area & perimeter of a rectangle")
    print("19. Calculate area of a circle")
    print("20. Calculate area of a triangle")
    print("21. Calculate net salary")
    print("22. Calculate net sales")
    print("23. Calculate average of three subjects")
    print("24. Swap two values")

    choice = int(input("Enter your choice (1-24): "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))
    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", subtract(a, b))
    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", multiply(a, b))
    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", divide(a, b))
    elif choice == 5:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        results = add_multiply_subtract_divide(a, b)
        print("Results:", results)
    elif choice == 6:
        hours = float(input("Enter hours: "))
        print("Minutes:", hours_to_minutes(hours))
    elif choice == 7:
        minutes = float(input("Enter minutes: "))
        print("Hours:", minutes_to_hours(minutes))
    elif choice == 8:
        dollars = float(input("Enter dollars: "))
        print("Rs.:", dollars_to_rs(dollars))
    elif choice == 9:
        rs = float(input("Enter Rs.: "))
        print("Dollars:", rs_to_dollars(rs))
    elif choice == 10:
        dollars = float(input("Enter dollars: "))
        print("Pounds:", dollars_to_pounds(dollars))
    elif choice == 11:
        grams = float(input("Enter grams: "))
        print("Kg:", grams_to_kg(grams))
    elif choice == 12:
        kgs = float(input("Enter kg: "))
        print("Grams:", kg_to_grams(kgs))
    elif choice == 13:
        bytes_value = float(input("Enter bytes: "))
        units = bytes_to_units(bytes_value)
        print("KB:", units["KB"], "MB:", units["MB"], "GB:", units["GB"])
    elif choice == 14:
        celsius = float(input("Enter Celsius: "))
        print("Fahrenheit:", celsius_to_fahrenheit(celsius))
    elif choice == 15:
        fahrenheit = float(input("Enter Fahrenheit: "))
        print("Celsius:", fahrenheit_to_celsius(fahrenheit))
    elif choice == 16:
        principal = float(input("Enter principal: "))
        rate = float(input("Enter rate: "))
        time = float(input("Enter time: "))
        print("Interest:", calculate_interest(principal, rate, time))
    elif choice == 17:
        side_length = float(input("Enter side length: "))
        results = square_area_perimeter(side_length)
        print("Area:", results["area"], "Perimeter:", results["perimeter"])
    elif choice == 18:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        results = rectangle_area_perimeter(length, breadth)
        print("Area:", results["area"], "Perimeter:", results["perimeter"])
    elif choice == 19:
        radius = float(input("Enter radius: "))
        print("Area:", circle_area(radius))
    elif choice == 20:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print("Area:", triangle_area(base, height))
    elif choice == 21:
        gross_salary = float(input("Enter gross salary: "))
        print("Net Salary:", calculate_net_salary(gross_salary))
    elif choice == 22:
        gross_sales = float(input("Enter gross sales: "))
        print("Net Sales:", calculate_net_sales(gross_sales))
    elif choice == 23:
        subject1 = float(input("Enter marks for subject 1: "))
        subject2 = float(input("Enter marks for subject 2: "))
        subject3 = float(input("Enter marks for subject 3: "))
        results = average_of_subjects(subject1, subject2, subject3)
        print("Total:", results["total"], "Average:", results["average"])
    elif choice == 24:
        a = float(input("Enter first value: "))
        b = float(input("Enter second value: "))
        swapped = swap(a, b)
        print("Swapped values:", swapped)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
