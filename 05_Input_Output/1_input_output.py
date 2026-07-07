"""
05 - Input and Output in Python

This file demonstrates:
1. print()
2. input()
3. Type Conversion
4. Multiple Inputs
5. f-Strings
6. sep Parameter
7. end Parameter
8. Escape Characters
"""

print("=" * 50)
print("      INPUT AND OUTPUT IN PYTHON")
print("=" * 50)

# ==========================================
# 1. print()
# ==========================================

print("\n1. print() Function")

print("Hello, World!")
print("Welcome to Python!")

# ==========================================
# 2. input()
# ==========================================

print("\n2. input() Function")

name = input("Enter your name: ")

print("Hello,", name)

# ==========================================
# 3. Type Conversion
# ==========================================

print("\n3. Type Conversion")

age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))

print("Age:", age)
print("Height:", height)

# ==========================================
# 4. Multiple Inputs
# ==========================================

print("\n4. Multiple Inputs")

city = input("Enter your city: ")
country = input("Enter your country: ")

print("City:", city)
print("Country:", country)

# ==========================================
# 5. Formatted Strings (f-strings)
# ==========================================

print("\n5. Formatted Strings")

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {city}, {country}.")

# ==========================================
# 6. sep Parameter
# ==========================================

print("\n6. sep Parameter")

print("Python", "Java", "C++", sep=" | ")

# ==========================================
# 7. end Parameter
# ==========================================

print("\n7. end Parameter")

print("Hello", end=" ")
print("World!")

# ==========================================
# 8. Escape Characters
# ==========================================

print("\n8. Escape Characters")

print("Hello\nWorld")
print("Python\tProgramming")
print("He said \"Hello\"")
print("C:\\Users\\Python")

print("\n" + "=" * 50)
print("        END OF INPUT & OUTPUT")
print("=" * 50)