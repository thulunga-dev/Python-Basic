"""
Challenge Solution: Number Analyzer
"""

print("=" * 50)
print("          NUMBER ANALYZER")
print("=" * 50)

# ==========================================
# Taking User Input
# ==========================================

number = int(input("Enter a positive integer: "))

# ==========================================
# Task 1: Print Numbers
# ==========================================

print("\nNumbers from 1 to", number)
print("-" * 50)

for i in range(1, number + 1):
    print(i, end=" ")

print()

# ==========================================
# Task 2: Sum of Numbers
# ==========================================

print("\nSum of Numbers")
print("-" * 50)

total = 0

for i in range(1, number + 1):
    total += i

print("Sum =", total)

# ==========================================
# Task 3: Even Numbers
# ==========================================

print("\nEven Numbers")
print("-" * 50)

for i in range(1, number + 1):
    if i % 2 == 0:
        print(i, end=" ")

print()

# ==========================================
# Task 4: Odd Numbers
# ==========================================

print("\nOdd Numbers")
print("-" * 50)

for i in range(1, number + 1):
    if i % 2 != 0:
        print(i, end=" ")

print()

# ==========================================
# Task 5: Multiplication Table
# ==========================================

print("\nMultiplication Table")
print("-" * 50)

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# ==========================================
# Task 6: Count Digits
# ==========================================

print("\nCount Digits")
print("-" * 50)

temp = number
digit_count = 0

while temp > 0:
    digit_count += 1
    temp //= 10

print("Total Digits:", digit_count)

# ==========================================
# Task 7: Reverse Number
# ==========================================

print("\nReverse Number")
print("-" * 50)

temp = number
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reversed Number:", reverse)

# ==========================================
# Task 8: Skip Multiples of 3
# ==========================================

print("\nSkip Multiples of 3")
print("-" * 50)

for i in range(1, number + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")

print()

# ==========================================
# Task 9: Stop at 20
# ==========================================

print("\nBreak at 20")
print("-" * 50)

for i in range(1, number + 1):
    if i == 20:
        print("Stopped at 20")
        break
    print(i, end=" ")

print()

# ==========================================
# Bonus 1: Triangle Pattern
# ==========================================

print("\nTriangle Pattern")
print("-" * 50)

for i in range(1, 6):
    print("*" * i)

# ==========================================
# Bonus 2: Count Even and Odd Numbers
# ==========================================

print("\nEven and Odd Count")
print("-" * 50)

even_count = 0
odd_count = 0

for i in range(1, number + 1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Numbers :", even_count)
print("Odd Numbers  :", odd_count)

# ==========================================
# Program Completed
# ==========================================

print("\n" + "=" * 50)
print("        LOOP CHALLENGE COMPLETED!")
print("=" * 50)