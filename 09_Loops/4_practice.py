"""
09 - Loops Practice

Practice programs for for loops, while loops,
and loop control statements.
"""

print("=" * 50)
print("          LOOPS PRACTICE")
print("=" * 50)

# ==========================================
# Practice 1: Print Numbers (1-10)
# ==========================================

print("\n1. Print Numbers (1-10)")
print("-" * 50)

for i in range(1, 11):
    print(i)

# ==========================================
# Practice 2: Print Even Numbers
# ==========================================

print("\n2. Even Numbers")
print("-" * 50)

for i in range(2, 21, 2):
    print(i)

# ==========================================
# Practice 3: Sum of First 10 Numbers
# ==========================================

print("\n3. Sum of First 10 Numbers")
print("-" * 50)

total = 0

for i in range(1, 11):
    total += i

print("Sum =", total)

# ==========================================
# Practice 4: Multiplication Table
# ==========================================

print("\n4. Multiplication Table of 7")
print("-" * 50)

for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# ==========================================
# Practice 5: Iterate Through a String
# ==========================================

print("\n5. Iterate Through a String")
print("-" * 50)

text = "Python"

for letter in text:
    print(letter)

# ==========================================
# Practice 6: while Loop
# ==========================================

print("\n6. while Loop")
print("-" * 50)

count = 1

while count <= 5:
    print(count)
    count += 1

# ==========================================
# Practice 7: Countdown
# ==========================================

print("\n7. Countdown")
print("-" * 50)

count = 5

while count >= 1:
    print(count)
    count -= 1

# ==========================================
# Practice 8: break Statement
# ==========================================

print("\n8. break Statement")
print("-" * 50)

for i in range(1, 11):
    if i == 6:
        break
    print(i)

# ==========================================
# Practice 9: continue Statement
# ==========================================

print("\n9. continue Statement")
print("-" * 50)

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# ==========================================
# Practice 10: pass Statement
# ==========================================

print("\n10. pass Statement")
print("-" * 50)

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

# ==========================================
# Practice 11: Search a Number
# ==========================================

print("\n11. Search a Number")
print("-" * 50)

numbers = [5, 10, 15, 20, 25]

target = 20

for number in numbers:
    if number == target:
        print("Number Found")
        break
else:
    print("Number Not Found")

# ==========================================
# Practice 12: Count Vowels
# ==========================================

print("\n12. Count Vowels")
print("-" * 50)

text = "Python Programming"

count = 0

for letter in text.lower():
    if letter in "aeiou":
        count += 1

print("Total Vowels:", count)

print("\n" + "=" * 50)
print("       PRACTICE COMPLETED")
print("=" * 50)