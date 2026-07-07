"""
03 - Data Types Practice

Practice Questions
"""

# ==========================================
# Practice 1: Integer
# ==========================================

age = 22

print("Age:", age)
print(type(age))

print("-" * 40)

# ==========================================
# Practice 2: Float
# ==========================================

height = 5.8

print("Height:", height)
print(type(height))

print("-" * 40)

# ==========================================
# Practice 3: String
# ==========================================

name = "Thulunga"

print("Name:", name)
print(type(name))

print("-" * 40)

# ==========================================
# Practice 4: Boolean
# ==========================================

is_student = True

print("Student:", is_student)
print(type(is_student))

print("-" * 40)

# ==========================================
# Practice 5: List
# ==========================================

languages = ["Python", "Java", "C++"]

print(languages)
print(type(languages))

print("-" * 40)

# ==========================================
# Practice 6: Tuple
# ==========================================

months = ("January", "February", "March")

print(months)
print(type(months))

print("-" * 40)

# ==========================================
# Practice 7: Set
# ==========================================

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))

print("-" * 40)

# ==========================================
# Practice 8: Dictionary
# ==========================================

student = {
    "name": "Thulunga",
    "age": 22,
    "course": "Computer Science"
}

print(student)
print(type(student))

print("-" * 40)

# ==========================================
# Practice 9: None
# ==========================================

result = None

print(result)
print(type(result))

print("-" * 40)

# ==========================================
# Practice 10: isinstance()
# ==========================================

print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(languages, list))
print(isinstance(student, dict))
