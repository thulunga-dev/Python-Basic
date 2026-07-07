"""
06 - Type Casting Practice
"""

print("=" * 50)
print("        TYPE CASTING PRACTICE")
print("=" * 50)

# ==========================================
# Practice 1: String to Integer
# ==========================================

number = "100"

print("Before:", number, type(number))

number = int(number)

print("After :", number, type(number))

print("-" * 50)

# ==========================================
# Practice 2: Integer to Float
# ==========================================

age = 22

print("Before:", age, type(age))

age = float(age)

print("After :", age, type(age))

print("-" * 50)

# ==========================================
# Practice 3: Float to Integer
# ==========================================

price = 99.99

print("Before:", price, type(price))

price = int(price)

print("After :", price, type(price))

print("-" * 50)

# ==========================================
# Practice 4: Integer to String
# ==========================================

marks = 95

print("Before:", marks, type(marks))

marks = str(marks)

print("After :", marks, type(marks))

print("-" * 50)

# ==========================================
# Practice 5: Boolean Conversion
# ==========================================

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))

print("-" * 50)

# ==========================================
# Practice 6: List Conversion
# ==========================================

fruits = ("Apple", "Banana", "Mango")

print("Tuple:", fruits)

fruits = list(fruits)

print("List :", fruits)

print("-" * 50)

# ==========================================
# Practice 7: Tuple Conversion
# ==========================================

numbers = [10, 20, 30]

print("List :", numbers)

numbers = tuple(numbers)

print("Tuple:", numbers)

print("-" * 50)

# ==========================================
# Practice 8: Set Conversion
# ==========================================

values = [1, 2, 2, 3, 3, 4]

print("List:", values)

values = set(values)

print("Set :", values)

print("-" * 50)

# ==========================================
# Practice 9: Dictionary Conversion
# ==========================================

student = [
    ("Name", "Thulunga"),
    ("Age", 22),
    ("Country", "India")
]

print(dict(student))

print("-" * 50)

# ==========================================
# Practice 10: User Input
# ==========================================

age = input("Enter your age: ")

print("Before:", age, type(age))

age = int(age)

print("After :", age, type(age))

print("=" * 50)
print("      PRACTICE COMPLETED")
print("=" * 50)
