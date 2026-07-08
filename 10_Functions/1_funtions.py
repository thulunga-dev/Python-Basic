"""
10 - Functions

This file demonstrates the basics of functions in Python.
"""

print("=" * 50)
print("            FUNCTIONS")
print("=" * 50)

# ==========================================
# 1. Defining and Calling a Function
# ==========================================

print("\n1. Defining and Calling a Function")
print("-" * 50)

def greet():
    print("Hello, Welcome to Python!")

greet()

# ==========================================
# 2. Function with Parameters
# ==========================================

print("\n2. Function with Parameters")
print("-" * 50)

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Thulunga")

# ==========================================
# 3. Function with Multiple Parameters
# ==========================================

print("\n3. Function with Multiple Parameters")
print("-" * 50)

def student(name, age):
    print(f"Name: {name}")
    print(f"Age : {age}")

student("Thulunga", 22)

# ==========================================
# 4. Function with Return Value
# ==========================================

print("\n4. Function with Return Value")
print("-" * 50)

def add(a, b):
    return a + b

result = add(10, 20)

print("Sum =", result)

# ==========================================
# 5. Default Parameters
# ==========================================

print("\n5. Default Parameters")
print("-" * 50)

def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Alice")

# ==========================================
# 6. Keyword Arguments
# ==========================================

print("\n6. Keyword Arguments")
print("-" * 50)

def employee(name, salary):
    print(f"Name   : {name}")
    print(f"Salary : {salary}")

employee(salary=50000, name="Rahul")

# ==========================================
# 7. Variable-Length Arguments (*args)
# ==========================================

print("\n7. *args")
print("-" * 50)

def total(*numbers):
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))

total(10, 20, 30, 40)

# ==========================================
# 8. Keyword Variable Arguments (**kwargs)
# ==========================================

print("\n8. **kwargs")
print("-" * 50)

def person(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

person(name="Thulunga", age=22, country="India")

# ==========================================
# 9. Local Variable
# ==========================================

print("\n9. Local Variable")
print("-" * 50)

def display():
    message = "I am a local variable."
    print(message)

display()

# ==========================================
# 10. Global Variable
# ==========================================

print("\n10. Global Variable")
print("-" * 50)

language = "Python"

def show_language():
    print("Language:", language)

show_language()

# ==========================================
# 11. Lambda Function
# ==========================================

print("\n11. Lambda Function")
print("-" * 50)

square = lambda x: x ** 2

print(square(5))

# ==========================================
# 12. Recursive Function
# ==========================================

print("\n12. Recursive Function")
print("-" * 50)

def countdown(number):
    if number == 0:
        return

    print(number)
    countdown(number - 1)

countdown(5)

print("\n" + "=" * 50)
print("      FUNCTIONS COMPLETED")
print("=" * 50)