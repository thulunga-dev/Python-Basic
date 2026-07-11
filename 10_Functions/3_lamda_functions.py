"""
10 - Lambda Functions

This file demonstrates lambda (anonymous) functions in Python.
"""

print("=" * 50)
print("         LAMBDA FUNCTIONS")
print("=" * 50)

# ==========================================
# 1. Basic Lambda Function
# ==========================================

print("\n1. Basic Lambda Function")
print("-" * 50)

square = lambda x: x ** 2

print(square(5))

# ==========================================
# 2. Lambda with Two Arguments
# ==========================================

print("\n2. Lambda with Two Arguments")
print("-" * 50)

add = lambda a, b: a + b

print(add(10, 20))

# ==========================================
# 3. Lambda with Three Arguments
# ==========================================

print("\n3. Lambda with Three Arguments")
print("-" * 50)

average = lambda a, b, c: (a + b + c) / 3

print(average(80, 90, 100))

# ==========================================
# 4. Lambda in sorted()
# ==========================================

print("\n4. Lambda with sorted()")
print("-" * 50)

students = [
    ("John", 80),
    ("Alice", 95),
    ("Bob", 75)
]

sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)

# ==========================================
# 5. Lambda with map()
# ==========================================

print("\n5. Lambda with map()")
print("-" * 50)

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)

# ==========================================
# 6. Lambda with filter()
# ==========================================

print("\n6. Lambda with filter()")
print("-" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

# ==========================================
# 7. Lambda with max()
# ==========================================

print("\n7. Lambda with max()")
print("-" * 50)

employees = [
    ("Rahul", 45000),
    ("Ankit", 55000),
    ("Priya", 50000)
]

highest_salary = max(employees, key=lambda employee: employee[1])

print(highest_salary)

# ==========================================
# 8. Lambda with min()
# ==========================================

print("\n8. Lambda with min()")
print("-" * 50)

lowest_salary = min(employees, key=lambda employee: employee[1])

print(lowest_salary)

# ==========================================
# 9. Conditional Lambda
# ==========================================

print("\n9. Conditional Lambda")
print("-" * 50)

even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"

print(even_or_odd(15))
print(even_or_odd(20))

# ==========================================
# 10. Immediately Invoked Lambda
# ==========================================

print("\n10. Immediately Invoked Lambda")
print("-" * 50)

print((lambda x, y: x * y)(5, 6))

print("\n" + "=" * 50)
print("      LAMBDA FUNCTIONS COMPLETED")
print("=" * 50)