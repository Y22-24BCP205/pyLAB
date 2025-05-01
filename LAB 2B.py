def largest_of_two(a, b):
    return max(a, b)

def smallest_of_two(a, b):
    return min(a, b)

def largest_of_three(a, b, c):
    return max(a, b, c)

def smallest_of_three(a, b, c):
    return min(a, b, c)

def is_even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def is_divisible_by_10(number):
    return number % 10 == 0

def check_age(age):
    return "Minor" if age < 18 else "Major"

def count_digits(number):
    return len(str(abs(number)))

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_triangle(angle1, angle2, angle3):
    return angle1 + angle2 + angle3 == 180

def absolute_value(number):
    return abs(number)

def compare_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area > perimeter

def are_points_collinear(x1, y1, x2, y2, x3, y3):
    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)

def point_in_circle(x, y, center_x, center_y, radius):
    distance_squared = (x - center_x) ** 2 + (y - center_y) ** 2
    radius_squared = radius ** 2
    if distance_squared < radius_squared:
        return "Inside"
    elif distance_squared == radius_squared:
        return "On"
    else:
        return "Outside"

def number_to_words(n):
    words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ]
    return words[n] if 0 <= n < 20 else "Out of range"

def calculate_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    grades = []
    for mark in marks:
        if mark < 0:
            grades.append("NA")
        elif mark <= 39:
            grades.append("F")
        elif mark <= 44:
            grades.append("P")
        elif mark <= 49:
            grades.append("C")
        elif mark <= 54:
            grades.append("B")
        elif mark <= 59:
            grades.append("B+")
        elif mark <= 69:
            grades.append("A")
        elif mark <= 79:
            grades.append("A+")
        elif mark <= 100:
            grades.append("O")
        else:
            grades.append("Invalid")
    return total, average, grades

def main():
    print("Select an operation:")
    print("1. Print largest and smallest values out of two")
    print("2. Print largest and smallest values out of three")
    print("3. Check whether a given number is odd or even")
    print("4. Check whether a given number is divisible by 10")
    print("5. Accept age of a person")
    print("6. Accept a number and print number of digits in it")
    print("7. Accept a year value and check if it is a leap year")
    print("8. Check whether a triangle is valid or not")
    print("9. Print absolute value of a given number")
    print("10. Compare area and perimeter of a rectangle")
    print("11. Check if three points fall on one straight line")
    print("12. Determine point's position relative to a circle")
    print("13. Convert number 0 to 19 to its equivalent words")
    print("14. Accept marks of three subjects and print total, average, and grades")

    choice = int(input("Enter your choice (1-14): "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Largest:", largest_of_two(a, b))
        print("Smallest:", smallest_of_two(a, b))
    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))
        print("Largest:", largest_of_three(a, b, c))
        print("Smallest:", smallest_of_three(a, b, c))
    elif choice == 3:
        number = int(input("Enter a number: "))
        print("The number is:", is_even_or_odd(number))
    elif choice == 4:
        number = int(input("Enter a number: "))
        print("Divisible by 10:", is_divisible_by_10(number))
    elif choice == 5:
        age = int(input("Enter age: "))
        print("Person is:", check_age(age))
    elif choice == 6:
        number = int(input("Enter a number: "))
        print("Number of digits:", count_digits(number))
    elif choice == 7:
        year = int(input("Enter a year: "))
        print("Leap year:", is_leap_year(year))
    elif choice == 8:
        angle1 = int(input("Enter first angle: "))
        angle2 = int(input("Enter second angle: "))
        angle3 = int(input("Enter third angle: "))
        print("Triangle is valid:", is_valid_triangle(angle1, angle2, angle3))
    elif choice == 9:
        number = float(input("Enter a number: "))
        print("Absolute value:", absolute_value(number))
    elif choice == 10:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        print("Area greater than perimeter:", compare_area_perimeter(length, breadth))
    elif choice == 11:
        x1, y1 = map(float, input("Enter coordinates of first point (x1 y1): ").split())
        x2, y2 = map(float, input("Enter coordinates of second point (x2 y2): ").split())
        x3, y3 = map(float, input("Enter coordinates of third point (x3 y3): ").split())
        print("Points are collinear:", are_points_collinear(x1, y1, x2, y2, x3, y3))
    elif choice == 12:
        x, y = map(float, input("Enter point coordinates (x y): ").split())
        center_x, center_y = map(float, input("Enter circle center coordinates (center_x center_y): ").split())
        radius = float(input("Enter radius: "))
        print("Point is:", point_in_circle(x, y, center_x, center_y, radius))
    elif choice == 13:
        n = int(input("Enter a number (0-19): "))
        print("Number in words:", number_to_words(n))
    elif choice == 14:
        marks = list(map(int, input("Enter marks for three subjects separated by space: ").split()))
        total, average, grades = calculate_marks(marks)
        print("Total:", total, "Average:", average, "Grades:", grades)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
