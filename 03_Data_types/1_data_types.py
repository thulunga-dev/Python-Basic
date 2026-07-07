"""
03 - Data Types in Python

This file demonstrates Python's built-in data types.
"""

print("=" * 50)
print("PYTHON DATA TYPES")
print("=" * 50)

# ==========================================
# 1. Integer (int)
# ==========================================

age = 22

print("\n1. Integer")
print(age)
print(type(age))

# ==========================================
# 2. Float (float)
# ==========================================

height = 5.8

print("\n2. Float")
print(height)
print(type(height))

# ==========================================
# 3. Complex (complex)
# ==========================================

number = 3 + 4j

print("\n3. Complex")
print(number)
print(type(number))

# ==========================================
# 4. Boolean (bool)
# ==========================================

is_student = True

print("\n4. Boolean")
print(is_student)
print(type(is_student))

# ==========================================
# 5. String (str)
# ==========================================

name = "Thulunga"

print("\n5. String")
print(name)
print(type(name))

# ==========================================
# 6. List (list)
# ==========================================

fruits = ["Apple", "Banana", "Mango"]

print("\n6. List")
print(fruits)
print(type(fruits))

# ==========================================
# 7. Tuple (tuple)
# ==========================================

colors = ("Red", "Green", "Blue")

print("\n7. Tuple")
print(colors)
print(type(colors))

# ==========================================
# 8. Set (set)
# ==========================================

numbers = {10, 20, 30, 40}

print("\n8. Set")
print(numbers)
print(type(numbers))

# ==========================================
# 9. Dictionary (dict)
# ==========================================

student = {
    "name": "Thulunga",
    "age": 22,
    "course": "Computer Science"
}

print("\n9. Dictionary")
print(student)
print(type(student))

# ==========================================
# 10. NoneType
# ==========================================

result = None

print("\n10. NoneType")
print(result)
print(type(result))

# ==========================================
# Checking Data Types
# ==========================================

print("\nUsing type()")

print(type(age))
print(type(height))
print(type(number))
print(type(is_student))
print(type(name))
print(type(fruits))
print(type(colors))
print(type(numbers))
print(type(student))
print(type(result))

# ==========================================
# Using isinstance()
# ==========================================

print("\nUsing isinstance()")

print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(fruits, list))
print(isinstance(student, dict))
