"""
04 - Operators Practice

Practice the different types of operators in Python.
"""

# ==========================================
# Practice 1: Arithmetic Operators
# ==========================================

a = 20
b = 6

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

print("-" * 40)

# ==========================================
# Practice 2: Assignment Operators
# ==========================================

x = 10

x += 5
print("x += 5 :", x)

x -= 3
print("x -= 3 :", x)

x *= 2
print("x *= 2 :", x)

print("-" * 40)

# ==========================================
# Practice 3: Comparison Operators
# ==========================================

num1 = 15
num2 = 20

print("Comparison Operators")
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

print("-" * 40)

# ==========================================
# Practice 4: Logical Operators
# ==========================================

age = 22
has_id = True

print("Logical Operators")
print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

print("-" * 40)

# ==========================================
# Practice 5: Identity Operators
# ==========================================

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("Identity Operators")
print(list1 is list2)
print(list1 is list3)
print(list1 is not list3)

print("-" * 40)

# ==========================================
# Practice 6: Membership Operators
# ==========================================

languages = ["Python", "Java", "C++"]

print("Membership Operators")
print("Python" in languages)
print("JavaScript" in languages)
print("JavaScript" not in languages)

print("-" * 40)

# ==========================================
# Practice 7: Bitwise Operators
# ==========================================

a = 10
b = 4

print("Bitwise Operators")
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)
