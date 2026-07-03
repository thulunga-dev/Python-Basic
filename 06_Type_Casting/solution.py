"""
Challenge Solution: Student Registration Form
"""

print("=" * 50)
print("      STUDENT REGISTRATION FORM")
print("=" * 50)

# ==========================================
# Taking User Input
# ==========================================

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))
weight = float(input("Enter your weight (in kg): "))
marks = int(input("Enter your marks: "))
enrolled = input("Are you enrolled (True/False): ") == "True"

# ==========================================
# Display Student Information
# ==========================================

print("\n" + "=" * 50)
print("            STUDENT DETAILS")
print("=" * 50)

print(f"Name      : {name}")
print(f"Age       : {age}")
print(f"Height    : {height} m")
print(f"Weight    : {weight} kg")
print(f"Marks     : {marks}")
print(f"Enrolled  : {enrolled}")

print("=" * 50)

# ==========================================
# Display Data Types
# ==========================================

print("\nData Types")
print("-" * 30)

print(f"Name      : {type(name)}")
print(f"Age       : {type(age)}")
print(f"Height    : {type(height)}")
print(f"Weight    : {type(weight)}")
print(f"Marks     : {type(marks)}")
print(f"Enrolled  : {type(enrolled)}")

# ==========================================
# Bonus Challenge
# ==========================================

print("\nBonus Challenge")
print("-" * 30)

# int -> float
age_float = float(age)
print("Age as Float:", age_float)

# int -> str
marks_string = str(marks)
print("Marks as String:", marks_string)

# str -> list
name_list = list(name)
print("Name as List:", name_list)

# list -> set
languages = ["Python", "Java", "Python", "C++"]
language_set = set(languages)
print("Languages as Set:", language_set)

# ==========================================
# Program Completed
# ==========================================

print("\n" + "=" * 50)
print("     TYPE CASTING CHALLENGE COMPLETED!")
print("=" * 50)