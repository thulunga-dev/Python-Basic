"""
Challenge Solution: Student Eligibility System
"""

print("=" * 50)
print("      STUDENT ELIGIBILITY SYSTEM")
print("=" * 50)

# ==========================================
# Taking User Input
# ==========================================

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

# ==========================================
# Pass or Fail
# ==========================================

if marks >= 40:
    result = "Pass"
else:
    result = "Fail"

# ==========================================
# Grade Calculation
# ==========================================

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

# ==========================================
# Scholarship Eligibility
# ==========================================

if marks >= 85 and attendance >= 90:
    scholarship = "Eligible"
else:
    scholarship = "Not Eligible"

# ==========================================
# Voting Eligibility
# ==========================================

if age >= 18:
    voting_status = "Eligible to Vote"
else:
    voting_status = "Not Eligible to Vote"

# ==========================================
# Attendance Check
# ==========================================

if attendance >= 75:
    attendance_status = "Good Attendance"
else:
    attendance_status = "Attendance Warning"

# ==========================================
# Ternary Operator
# ==========================================

age_group = "Adult" if age >= 18 else "Minor"

# ==========================================
# Nested if
# ==========================================

if result == "Pass":
    if scholarship == "Eligible":
        message = "Congratulations! You received a scholarship."
    else:
        message = "You passed, but you are not eligible for a scholarship."
else:
    message = "Improve your marks."

# ==========================================
# Display Student Report
# ==========================================

print("\n" + "=" * 50)
print("            STUDENT REPORT")
print("=" * 50)

print(f"Name              : {name}")
print(f"Age               : {age}")
print(f"Marks             : {marks}")
print(f"Attendance        : {attendance}%")

print("-" * 50)

print(f"Result            : {result}")
print(f"Grade             : {grade}")
print(f"Scholarship       : {scholarship}")
print(f"Voting Status     : {voting_status}")
print(f"Attendance Status : {attendance_status}")
print(f"Age Group         : {age_group}")

print("-" * 50)

print(f"Message           : {message}")

print("=" * 50)
print(" CONDITIONAL STATEMENTS CHALLENGE COMPLETED ")
print("=" * 50)