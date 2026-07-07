"""
Challenge Solution: Student Profile Using Python Data Types
"""

# ==========================================
# Creating Variables
# ==========================================

# String
name = "Thulunga"

# Integer
age = 22

# Float
height = 5.8

# Complex
complex_number = 4 + 3j

# Boolean
is_student = True

# List
languages = ["Python", "Java", "C++"]

# Tuple
favorite_colors = ("Blue", "Black", "White")

# Set
hobbies = {"Coding", "Reading", "Watching Anime"}

# Dictionary
student_info = {
    "Name": name,
    "Age": age,
    "Course": "Computer Science",
    "Country": "India"
}

# None
future_job = None

# ==========================================
# Display Student Profile
# ==========================================

print("=" * 50)
print("               STUDENT PROFILE")
print("=" * 50)

print(f"Name            : {name}")
print(f"Age             : {age}")
print(f"Height          : {height}")
print(f"Complex Number  : {complex_number}")
print(f"Student         : {is_student}")
print(f"Languages       : {languages}")
print(f"Favorite Colors : {favorite_colors}")
print(f"Hobbies         : {hobbies}")
print(f"Student Info    : {student_info}")
print(f"Future Job      : {future_job}")

print("=" * 50)

# ==========================================
# Display Data Types
# ==========================================

print("\nData Types")
print("-" * 30)

print(type(name))
print(type(age))
print(type(height))
print(type(complex_number))
print(type(is_student))
print(type(languages))
print(type(favorite_colors))
print(type(hobbies))
print(type(student_info))
print(type(future_job))

# ==========================================
# Using isinstance()
# ==========================================

print("\nUsing isinstance()")
print("-" * 30)

print(isinstance(name, str))
print(isinstance(age, int))
print(isinstance(height, float))
print(isinstance(complex_number, complex))
print(isinstance(is_student, bool))
print(isinstance(languages, list))
print(isinstance(favorite_colors, tuple))
print(isinstance(hobbies, set))
print(isinstance(student_info, dict))
print(isinstance(future_job, type(None)))
