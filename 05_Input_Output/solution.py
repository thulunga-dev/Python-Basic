"""
Challenge Solution: Student Information System
"""

print("=" * 50)
print("        STUDENT INFORMATION SYSTEM")
print("=" * 50)

# ==========================================
# Taking Input
# ==========================================

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))
course = input("Enter your course: ")
city = input("Enter your city: ")
country = input("Enter your country: ")

# ==========================================
# Display Student Information
# ==========================================

print("\n" + "=" * 50)
print("           STUDENT INFORMATION")
print("=" * 50)

print(f"Name      : {name}")
print(f"Age       : {age}")
print(f"Height    : {height} m")
print(f"Course    : {course}")
print(f"City      : {city}")
print(f"Country   : {country}")

print("=" * 50)

# ==========================================
# Display Data Types
# ==========================================

print("\nData Types")
print("-" * 30)

print(f"Age Type    : {type(age)}")
print(f"Height Type : {type(height)}")

# ==========================================
# Using sep
# ==========================================

print("\nUsing sep")
print("-" * 30)

print(name, course, country, sep=" | ")

# ==========================================
# Using end
# ==========================================

print("\nUsing end")
print("-" * 30)

print("Welcome", end=" ")
print("to", end=" ")
print("Python!")

# ==========================================
# Escape Characters
# ==========================================

print("\n\nEscape Characters")
print("-" * 30)

print("Hello\nWorld")
print("Python\tProgramming")
print("He said \"Welcome to Python!\"")

print("\n" + "=" * 50)
print("      CHALLENGE COMPLETED SUCCESSFULLY!")
print("=" * 50)