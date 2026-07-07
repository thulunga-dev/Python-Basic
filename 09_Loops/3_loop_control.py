"""
09 - Loop Control Statements

This file demonstrates loop control statements in Python.
"""

print("=" * 50)
print("       LOOP CONTROL STATEMENTS")
print("=" * 50)

# ==========================================
# 1. break Statement
# ==========================================

print("\n1. break Statement")
print("-" * 50)

for i in range(1, 11):
    if i == 6:
        break
    print(i)

# ==========================================
# 2. continue Statement
# ==========================================

print("\n2. continue Statement")
print("-" * 50)

for i in range(1, 11):
    if i == 6:
        continue
    print(i)

# ==========================================
# 3. pass Statement
# ==========================================

print("\n3. pass Statement")
print("-" * 50)

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

# ==========================================
# 4. break in while Loop
# ==========================================

print("\n4. break in while Loop")
print("-" * 50)

count = 1

while True:
    print(count)

    if count == 5:
        break

    count += 1

# ==========================================
# 5. continue in while Loop
# ==========================================

print("\n5. continue in while Loop")
print("-" * 50)

count = 0

while count < 10:
    count += 1

    if count == 5:
        continue

    print(count)

# ==========================================
# 6. pass in while Loop
# ==========================================

print("\n6. pass in while Loop")
print("-" * 50)

count = 1

while count <= 5:
    if count == 3:
        pass

    print(count)
    count += 1

# ==========================================
# 7. for...else
# ==========================================

print("\n7. for...else")
print("-" * 50)

for i in range(1, 6):
    print(i)
else:
    print("Loop Completed Successfully")

# ==========================================
# 8. while...else
# ==========================================

print("\n8. while...else")
print("-" * 50)

count = 1

while count <= 5:
    print(count)
    count += 1
else:
    print("Loop Completed Successfully")

# ==========================================
# 9. Search Example using break
# ==========================================

print("\n9. Search Example")
print("-" * 50)

numbers = [10, 20, 30, 40, 50]

target = 30

for number in numbers:
    if number == target:
        print(f"{target} Found!")
        break
else:
    print("Number Not Found")

# ==========================================
# 10. Skip Even Numbers
# ==========================================

print("\n10. Skip Even Numbers")
print("-" * 50)

for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)

print("\n" + "=" * 50)
print("    LOOP CONTROL COMPLETED")
print("=" * 50)