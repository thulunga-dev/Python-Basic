"""
09 - While Loop

This file demonstrates the basics of the while loop in Python.
"""

print("=" * 50)
print("           WHILE LOOP")
print("=" * 50)

# ==========================================
# 1. Basic while Loop
# ==========================================

print("\n1. Basic while Loop")
print("-" * 50)

count = 1

while count <= 5:
    print(count)
    count += 1

# ==========================================
# 2. Print Even Numbers
# ==========================================

print("\n2. Print Even Numbers")
print("-" * 50)

number = 2

while number <= 10:
    print(number)
    number += 2

# ==========================================
# 3. Print Odd Numbers
# ==========================================

print("\n3. Print Odd Numbers")
print("-" * 50)

number = 1

while number <= 10:
    print(number)
    number += 2

# ==========================================
# 4. Reverse Counting
# ==========================================

print("\n4. Reverse Counting")
print("-" * 50)

count = 5

while count >= 1:
    print(count)
    count -= 1

# ==========================================
# 5. Sum of First 10 Numbers
# ==========================================

print("\n5. Sum of First 10 Numbers")
print("-" * 50)

count = 1
total = 0

while count <= 10:
    total += count
    count += 1

print("Sum =", total)

# ==========================================
# 6. Multiplication Table
# ==========================================

print("\n6. Multiplication Table")
print("-" * 50)

number = 5
i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

# ==========================================
# 7. Loop Through a String
# ==========================================

print("\n7. Loop Through a String")
print("-" * 50)

text = "Python"
index = 0

while index < len(text):
    print(text[index])
    index += 1

# ==========================================
# 8. while...else
# ==========================================

print("\n8. while...else")
print("-" * 50)

count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Loop Finished Successfully")

# ==========================================
# 9. Infinite Loop (Example)
# ==========================================

print("\n9. Infinite Loop")
print("-" * 50)

print("Example (Do NOT run):")

"""
while True:
    print("This loop runs forever.")
"""

# ==========================================
# 10. User-Controlled Loop
# ==========================================

print("\n10. User-Controlled Loop")
print("-" * 50)

choice = "yes"

while choice.lower() == "yes":
    print("Loop is running...")
    choice = input("Do you want to continue? (yes/no): ")

print("Loop Ended.")

print("\n" + "=" * 50)
print("        WHILE LOOP COMPLETED")
print("=" * 50)