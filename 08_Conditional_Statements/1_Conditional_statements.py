"""
08 - Conditional Statements

This file demonstrates the basics of conditional statements in Python.
"""

print("=" * 50)
print("      CONDITIONAL STATEMENTS")
print("=" * 50)

# ==========================================
# 1. Simple if Statement
# ==========================================

print("\n1. Simple if Statement")
print("-" * 50)

age = 20

if age >= 18:
    print("You are an adult.")

# ==========================================
# 2. if...else Statement
# ==========================================

print("\n2. if...else Statement")
print("-" * 50)

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

# ==========================================
# 3. if...elif...else Statement
# ==========================================

print("\n3. if...elif...else Statement")
print("-" * 50)

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# ==========================================
# 4. Nested if Statement
# ==========================================

print("\n4. Nested if Statement")
print("-" * 50)

age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")

# ==========================================
# 5. Logical Operators
# ==========================================

print("\n5. Logical Operators")
print("-" * 50)

age = 20
has_license = True

# and
if age >= 18 and has_license:
    print("You can drive.")

# or
temperature = 38

if temperature > 35 or temperature < 10:
    print("Extreme weather.")

# not
is_logged_in = False

if not is_logged_in:
    print("Please log in.")

# ==========================================
# 6. Ternary Operator
# ==========================================

print("\n6. Ternary Operator")
print("-" * 50)

age = 17

status = "Adult" if age >= 18 else "Minor"

print(status)

# ==========================================
# 7. Multiple Conditions
# ==========================================

print("\n7. Multiple Conditions")
print("-" * 50)

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")

# ==========================================
# 8. Membership Operator with if
# ==========================================

print("\n8. Membership Operator")
print("-" * 50)

language = "Python"

if "Py" in language:
    print("Substring Found")
else:
    print("Substring Not Found")

# ==========================================
# 9. Comparison Operators
# ==========================================

print("\n9. Comparison Operators")
print("-" * 50)

a = 10
b = 20

if a < b:
    print("a is smaller than b")

if a != b:
    print("a and b are different")

# ==========================================
# 10. Real-World Example
# ==========================================

print("\n10. Real-World Example")
print("-" * 50)

balance = 5000
withdraw = 3000

if withdraw <= balance:
    balance -= withdraw
    print("Transaction Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")

print("\n" + "=" * 50)
print("   CONDITIONAL STATEMENTS COMPLETED")
print("=" * 50)