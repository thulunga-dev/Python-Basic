"""
09 - For Loop

This file demonstrates the basics of the for loop in Python.
"""

print("=" * 50)
print("            FOR LOOP")
print("=" * 50)

# ==========================================
# 1. Basic for Loop
# ==========================================

print("\n1. Basic for Loop")
print("-" * 50)

for i in range(5):
    print(i)

# ==========================================
# 2. range(start, stop)
# ==========================================

print("\n2. range(start, stop)")
print("-" * 50)

for i in range(1, 6):
    print(i)

# ==========================================
# 3. range(start, stop, step)
# ==========================================

print("\n3. range(start, stop, step)")
print("-" * 50)

for i in range(2, 11, 2):
    print(i)

# ==========================================
# 4. Reverse Loop
# ==========================================

print("\n4. Reverse Loop")
print("-" * 50)

for i in range(5, 0, -1):
    print(i)

# ==========================================
# 5. Loop Through a String
# ==========================================

print("\n5. Loop Through a String")
print("-" * 50)

language = "Python"

for letter in language:
    print(letter)

# ==========================================
# 6. Loop Through a List
# ==========================================

print("\n6. Loop Through a List")
print("-" * 50)

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# ==========================================
# 7. Loop Through a Tuple
# ==========================================

print("\n7. Loop Through a Tuple")
print("-" * 50)

numbers = (10, 20, 30)

for number in numbers:
    print(number)

# ==========================================
# 8. Loop Through a Set
# ==========================================

print("\n8. Loop Through a Set")
print("-" * 50)

colors = {"Red", "Green", "Blue"}

for color in colors:
    print(color)

# ==========================================
# 9. Loop Through a Dictionary
# ==========================================

print("\n9. Loop Through a Dictionary")
print("-" * 50)

student = {
    "Name": "Thulunga",
    "Age": 22,
    "Course": "Python"
}

print("Keys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# ==========================================
# 10. Using else with for Loop
# ==========================================

print("\n10. for...else")
print("-" * 50)

for i in range(1, 6):
    print(i)
else:
    print("Loop Finished Successfully")

print("\n" + "=" * 50)
print("         FOR LOOP COMPLETED")
print("=" * 50)