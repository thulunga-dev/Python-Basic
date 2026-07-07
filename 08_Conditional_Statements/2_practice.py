"""
08 - Conditional Statements Practice
"""

print("=" * 50)
print("      CONDITIONAL STATEMENTS PRACTICE")
print("=" * 50)

# ==========================================
# Practice 1: Check Positive Number
# ==========================================

print("\n1. Check Positive Number")

number = 15

if number > 0:
    print("Positive Number")

# ==========================================
# Practice 2: Even or Odd
# ==========================================

print("\n2. Even or Odd")

number = 12

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# ==========================================
# Practice 3: Voting Eligibility
# ==========================================

print("\n3. Voting Eligibility")

age = 20

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

# ==========================================
# Practice 4: Grade Calculator
# ==========================================

print("\n4. Grade Calculator")

marks = 76

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# ==========================================
# Practice 5: Largest Number
# ==========================================

print("\n5. Largest Number")

a = 15
b = 28

if a > b:
    print(f"{a} is larger")
else:
    print(f"{b} is larger")

# ==========================================
# Practice 6: Nested if
# ==========================================

print("\n6. Nested if")

age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Under Age")

# ==========================================
# Practice 7: Logical Operators
# ==========================================

print("\n7. Logical Operators")

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Login")

# ==========================================
# Practice 8: Membership Operator
# ==========================================

print("\n8. Membership Operator")

language = "Python Programming"

if "Python" in language:
    print("Python Found")
else:
    print("Python Not Found")

# ==========================================
# Practice 9: Ternary Operator
# ==========================================

print("\n9. Ternary Operator")

age = 17

status = "Adult" if age >= 18 else "Minor"

print(status)

# ==========================================
# Practice 10: ATM Withdrawal
# ==========================================

print("\n10. ATM Withdrawal")

balance = 10000
withdraw = 3500

if withdraw <= balance:
    balance -= withdraw
    print("Transaction Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")

print("\n" + "=" * 50)
print("     PRACTICE COMPLETED")
print("=" * 50)