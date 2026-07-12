"""
Challenge Solution: Student Result Management System
"""

print("=" * 50)
print("      STUDENT RESULT MANAGEMENT")
print("=" * 50)

# ==========================================
# User Input
# ==========================================

name = input("Enter student name: ")

python_marks = float(input("Enter Python marks: "))
sql_marks = float(input("Enter SQL marks: "))
math_marks = float(input("Enter Mathematics marks: "))

# ==========================================
# Function 1: Calculate Total
# ==========================================

def calculate_total(python, sql, math):
    return python + sql + math

# ==========================================
# Function 2: Calculate Average
# ==========================================

def calculate_average(total):
    return total / 3

# ==========================================
# Function 3: Calculate Grade
# ==========================================

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

# ==========================================
# Function 4: Check Result
# ==========================================

def check_result(average):
    if average >= 40:
        return "Pass"
    return "Fail"

# ==========================================
# Function 5: Display Report
# ==========================================

def display_report():
    print("\n" + "=" * 50)
    print("             STUDENT REPORT")
    print("=" * 50)

    print(f"Name            : {name}")
    print(f"Python Marks    : {python_marks}")
    print(f"SQL Marks       : {sql_marks}")
    print(f"Math Marks      : {math_marks}")

    print("-" * 50)

    print(f"Total           : {total}")
    print(f"Average         : {average:.2f}")
    print(f"Grade           : {grade}")
    print(f"Result          : {result}")

    print("=" * 50)

# ==========================================
# Bonus 1: Default Argument
# ==========================================

def welcome(student="Guest"):
    print(f"\nWelcome, {student}!")

# ==========================================
# Bonus 2: *args
# ==========================================

def add_numbers(*numbers):
    return sum(numbers)

# ==========================================
# Bonus 3: **kwargs
# ==========================================

def student_info(**details):
    print("\nStudent Information")

    for key, value in details.items():
        print(f"{key}: {value}")

# ==========================================
# Bonus 4: Lambda Function
# ==========================================

square = lambda number: number ** 2

# ==========================================
# Bonus 5: Recursive Function
# ==========================================

def countdown(number):
    if number == 0:
        return

    print(number)
    countdown(number - 1)

# ==========================================
# Function Calls
# ==========================================

total = calculate_total(
    python_marks,
    sql_marks,
    math_marks
)

average = calculate_average(total)

grade = calculate_grade(average)

result = check_result(average)

display_report()

welcome(name)

print("\nSum using *args:", add_numbers(10, 20, 30, 40))

student_info(
    Name=name,
    Course="Python",
    Country="India"
)

print("\nSquare of 8:", square(8))

print("\nCountdown")

countdown(5)

print("\n" + "=" * 50)
print("     FUNCTIONS CHALLENGE COMPLETED")
print("=" * 50)