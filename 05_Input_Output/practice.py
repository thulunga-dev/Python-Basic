"""
05 - Input and Output Practice
"""

print("=" * 50)
print("        INPUT AND OUTPUT PRACTICE")
print("=" * 50)

# ==========================================
# Practice 1: print()
# ==========================================

print("\nPractice 1")

print("Hello, World!")
print("Welcome to Python!")

# ==========================================
# Practice 2: input()
# ==========================================

print("\nPractice 2")

name = input("Enter your name: ")

print("Hello,", name)

# ==========================================
# Practice 3: Integer Input
# ==========================================

print("\nPractice 3")

age = int(input("Enter your age: "))

print(f"You are {age} years old.")

# ==========================================
# Practice 4: Float Input
# ==========================================

print("\nPractice 4")

height = float(input("Enter your height (in meters): "))

print(f"Your height is {height} meters.")

# ==========================================
# Practice 5: Multiple Inputs
# ==========================================

print("\nPractice 5")

city = input("Enter your city: ")
country = input("Enter your country: ")

print(f"You live in {city}, {country}.")

# ==========================================
# Practice 6: f-string
# ==========================================

print("\nPractice 6")

course = input("Enter your course: ")

print(f"I am studying {course}.")

# ==========================================
# Practice 7: sep Parameter
# ==========================================

print("\nPractice 7")

print("Python", "Java", "C++", sep=" | ")

# ==========================================
# Practice 8: end Parameter
# ==========================================

print("\nPractice 8")

print("Hello", end=" ")
print("World!")

# ==========================================
# Practice 9: Escape Characters
# ==========================================

print("\nPractice 9")

print("Python\nProgramming")
print("Python\tProgramming")
print("He said \"Hello\"")

# ==========================================
# Practice 10: Student Profile
# ==========================================

print("\nPractice 10")

student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
student_course = input("Enter your course: ")

print("\nStudent Details")
print("-" * 30)
print(f"Name   : {student_name}")
print(f"Age    : {student_age}")
print(f"Course : {student_course}")