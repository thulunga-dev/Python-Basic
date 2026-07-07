"""
02 - Variables in Python

This file demonstrates:
1. Creating variables
2. Variable naming
3. Multiple assignment
4. Dynamic typing
5. Reassignment
6. Swapping variables
7. Type checking
8. Memory identity
9. Deleting variables
"""

# ==========================================
# 1. Creating Variables
# ==========================================

name = "Thulunga"
age = 22
height = 5.8
is_student = True

print("Creating Variables")
print(name)
print(age)
print(height)
print(is_student)

print("-" * 40)


# ==========================================
# 2. Variable Naming
# ==========================================

student_name = "John"
total_marks = 95
country = "India"

print("Variable Naming")
print(student_name)
print(total_marks)
print(country)

print("-" * 40)


# ==========================================
# 3. Multiple Assignment
# ==========================================

x = y = z = 100

print("Multiple Assignment")
print(x)
print(y)
print(z)

print("-" * 40)

a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

print("-" * 40)


# ==========================================
# 4. Dynamic Typing
# ==========================================

value = 100
print("Dynamic Typing")
print(value)
print(type(value))

value = "Python"
print(value)
print(type(value))

value = 3.14
print(value)
print(type(value))

print("-" * 40)


# ==========================================
# 5. Variable Reassignment
# ==========================================

city = "Delhi"

print("Before:", city)

city = "Guwahati"

print("After :", city)

print("-" * 40)


# ==========================================
# 6. Swapping Variables
# ==========================================

num1 = 10
num2 = 20

print("Before Swapping")
print(num1, num2)

num1, num2 = num2, num1

print("After Swapping")
print(num1, num2)

print("-" * 40)


# ==========================================
# 7. Type Checking
# ==========================================

language = "Python"

print("Type Checking")
print(type(language))
print(type(age))
print(type(height))
print(type(is_student))

print("-" * 40)


# ==========================================
# 8. Object Identity
# ==========================================

number = 50

print("Object Identity")
print(id(number))

print("-" * 40)


# ==========================================
# 9. Deleting Variables
# ==========================================

temp = "Temporary Variable"

print(temp)

del temp

# Uncomment the next line to see the error
# print(temp)

print("-" * 40)


# ==========================================
# 10. Constants (Naming Convention)
# ==========================================

PI = 3.14159
MAX_USERS = 100

print("Constants")
print(PI) 
print(MAX_USERS)
