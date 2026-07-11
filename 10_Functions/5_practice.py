"""
10 - Functions Practice

Practice programs for Python functions.
"""

print("=" * 50)
print("         FUNCTIONS PRACTICE")
print("=" * 50)

# ==========================================
# Practice 1: Simple Function
# ==========================================

print("\n1. Simple Function")
print("-" * 50)

def greet():
    print("Hello, Python!")

greet()

# ==========================================
# Practice 2: Function with Parameter
# ==========================================

print("\n2. Function with Parameter")
print("-" * 50)

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Thulunga")

# ==========================================
# Practice 3: Multiple Parameters
# ==========================================

print("\n3. Multiple Parameters")
print("-" * 50)

def student(name, age, course):
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Course : {course}")

student("Thulunga", 22, "Python")

# ==========================================
# Practice 4: Return Statement
# ==========================================

print("\n4. Return Statement")
print("-" * 50)

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)

# ==========================================
# Practice 5: Default Parameter
# ==========================================

print("\n5. Default Parameter")
print("-" * 50)

def greet(name="Guest"):
    print(f"Welcome, {name}")

greet()
greet("Alice")

# ==========================================
# Practice 6: Keyword Arguments
# ==========================================

print("\n6. Keyword Arguments")
print("-" * 50)

def employee(name, salary):
    print(f"Name   : {name}")
    print(f"Salary : {salary}")

employee(salary=50000, name="Rahul")

# ==========================================
# Practice 7: *args
# ==========================================

print("\n7. *args")
print("-" * 50)

def total(*numbers):
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))

total(10, 20, 30, 40)

# ==========================================
# Practice 8: **kwargs
# ==========================================

print("\n8. **kwargs")
print("-" * 50)

def person(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

person(name="Thulunga", age=22, country="India")

# ==========================================
# Practice 9: Local & Global Variables
# ==========================================

print("\n9. Local & Global Variables")
print("-" * 50)

language = "Python"

def display():
    message = "Local Variable"
    print(message)
    print(language)

display()

# ==========================================
# Practice 10: Lambda Function
# ==========================================

print("\n10. Lambda Function")
print("-" * 50)

square = lambda x: x ** 2

print("Square =", square(6))

# ==========================================
# Practice 11: Recursive Function
# ==========================================

print("\n11. Recursive Function")
print("-" * 50)

def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)

countdown(5)

# ==========================================
# Practice 12: Area of Rectangle
# ==========================================

print("\n12. Area of Rectangle")
print("-" * 50)

def area(length, width):
    return length * width

print("Area =", area(10, 5))

print("\n" + "=" * 50)
print("      PRACTICE COMPLETED")
print("=" * 50)