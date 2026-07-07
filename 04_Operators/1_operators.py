"""
04 - Operators in Python

This file demonstrates all Python operators with examples.
"""

print("=" * 50)
print("        PYTHON OPERATORS")
print("=" * 50)

# ==========================================
# 1. Arithmetic Operators
# ==========================================

print("\n1. Arithmetic Operators")

a = 10
b = 3

print(f"a = {a}, b = {b}")

print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Exponentiation (**):", a ** b)

# ==========================================
# 2. Assignment Operators
# ==========================================

print("\n2. Assignment Operators")

x = 10
print("Initial Value:", x)

x += 5
print("x += 5 :", x)

x -= 2
print("x -= 2 :", x)

x *= 3
print("x *= 3 :", x)

x /= 2
print("x /= 2 :", x)

x //= 2
print("x //= 2 :", x)

x %= 3
print("x %= 3 :", x)

x **= 2
print("x **= 2 :", x)

# ==========================================
# 3. Comparison Operators
# ==========================================

print("\n3. Comparison Operators")

a = 10
b = 5

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# ==========================================
# 4. Logical Operators
# ==========================================

print("\n4. Logical Operators")

x = True
y = False

print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)

# ==========================================
# 5. Identity Operators
# ==========================================

print("\n5. Identity Operators")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 is not list3 :", list1 is not list3)

# ==========================================
# 6. Membership Operators
# ==========================================

print("\n6. Membership Operators")

fruits = ["Apple", "Banana", "Mango"]

print("'Apple' in fruits :", "Apple" in fruits)
print("'Orange' in fruits :", "Orange" in fruits)
print("'Orange' not in fruits :", "Orange" not in fruits)

# ==========================================
# 7. Bitwise Operators
# ==========================================

print("\n7. Bitwise Operators")

a = 5
b = 3

print("a & b :", a & b)
print("a | b :", a | b)
print("a ^ b :", a ^ b)
print("~a    :", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)
