"""
06 - Type Casting in Python

This file demonstrates implicit and explicit type casting
using Python's built-in conversion functions.
"""

print("=" * 50)
print("          TYPE CASTING")
print("=" * 50)

# ==========================================
# 1. Implicit Type Casting
# ==========================================

print("\n1. Implicit Type Casting")
print("-" * 30)

num1 = 10
num2 = 5.5

result = num1 + num2

print("num1:", num1)
print("num2:", num2)
print("Result:", result)
print("Type of result:", type(result))

# ==========================================
# 2. Explicit Type Casting
# ==========================================

print("\n2. Explicit Type Casting")
print("-" * 30)

age = "22"

print("Before:", age, type(age))

age = int(age)

print("After :", age, type(age))

# ==========================================
# 3. int()
# ==========================================

print("\n3. int()")
print("-" * 30)

print(int(5.9))
print(int(True))
print(int(False))

# ==========================================
# 4. float()
# ==========================================

print("\n4. float()")
print("-" * 30)

print(float(10))
print(float(True))
print(float(False))

# ==========================================
# 5. str()
# ==========================================

print("\n5. str()")
print("-" * 30)

print(str(100))
print(str(10.5))
print(str(True))

# ==========================================
# 6. bool()
# ==========================================

print("\n6. bool()")
print("-" * 30)

print(bool(1))
print(bool(0))
print(bool(-5))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2, 3]))

# ==========================================
# 7. list()
# ==========================================

print("\n7. list()")
print("-" * 30)

numbers = (10, 20, 30)

print(list(numbers))

text = "Python"

print(list(text))

# ==========================================
# 8. tuple()
# ==========================================

print("\n8. tuple()")
print("-" * 30)

numbers = [1, 2, 3]

print(tuple(numbers))

# ==========================================
# 9. set()
# ==========================================

print("\n9. set()")
print("-" * 30)

numbers = [1, 2, 2, 3, 4, 4]

print(set(numbers))

# ==========================================
# 10. dict()
# ==========================================

print("\n10. dict()")
print("-" * 30)

student = [
    ("name", "Thulunga"),
    ("age", 22),
    ("course", "Computer Science")
]

print(dict(student))

# ==========================================
# 11. Invalid Type Casting
# ==========================================

print("\n11. Invalid Type Casting")
print("-" * 30)

print("The following conversions will produce an error:")

# Uncomment to see the errors

# int("Hello")
# float("Python")
# int([1, 2, 3])

print("\nAvoid converting incompatible data types.")

print("\n" + "=" * 50)
print("      TYPE CASTING COMPLETED")
print("=" * 50)
