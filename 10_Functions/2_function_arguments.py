"""
10 - Function Arguments

This file demonstrates different types of function arguments in Python.
"""

print("=" * 50)
print("         FUNCTION ARGUMENTS")
print("=" * 50)

# ==========================================
# 1. Positional Arguments
# ==========================================

print("\n1. Positional Arguments")
print("-" * 50)

def student(name, age):
    print(f"Name: {name}")
    print(f"Age : {age}")

student("Thulunga", 22)

# ==========================================
# 2. Keyword Arguments
# ==========================================

print("\n2. Keyword Arguments")
print("-" * 50)

student(age=22, name="Thulunga")

# ==========================================
# 3. Default Arguments
# ==========================================

print("\n3. Default Arguments")
print("-" * 50)

def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Alice")

# ==========================================
# 4. Multiple Default Arguments
# ==========================================

print("\n4. Multiple Default Arguments")
print("-" * 50)

def employee(name, salary=30000, city="Delhi"):
    print(f"Name   : {name}")
    print(f"Salary : {salary}")
    print(f"City   : {city}")

employee("Rahul")
employee("Ankit", 50000)
employee("Priya", 60000, "Mumbai")

# ==========================================
# 5. Variable-Length Arguments (*args)
# ==========================================

print("\n5. *args")
print("-" * 50)

def add_numbers(*numbers):
    print("Arguments:", numbers)
    print("Sum:", sum(numbers))

add_numbers(10, 20)
add_numbers(10, 20, 30, 40)

# ==========================================
# 6. Keyword Variable Arguments (**kwargs)
# ==========================================

print("\n6. **kwargs")
print("-" * 50)

def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(
    name="Thulunga",
    age=22,
    course="Python",
    country="India"
)

# ==========================================
# 7. Mixing Different Types of Arguments
# ==========================================

print("\n7. Mixed Arguments")
print("-" * 50)

def details(name, age=18, *skills, **info):
    print(f"Name : {name}")
    print(f"Age  : {age}")
    print(f"Skills : {skills}")
    print(f"Extra Info : {info}")

details(
    "Thulunga",
    22,
    "Python",
    "SQL",
    city="Kokrajhar",
    country="India"
)

# ==========================================
# 8. Return Values with Arguments
# ==========================================

print("\n8. Return Value")
print("-" * 50)

def multiply(a, b):
    return a * b

result = multiply(5, 8)

print("Result:", result)

print("\n" + "=" * 50)
print("    FUNCTION ARGUMENTS COMPLETED")
print("=" * 50)