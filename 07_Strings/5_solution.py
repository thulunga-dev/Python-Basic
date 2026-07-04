"""
Challenge Solution: Student String Analyzer
"""

print("=" * 50)
print("      STUDENT STRING ANALYZER")
print("=" * 50)

# ==========================================
# Taking User Input
# ==========================================

name = input("Enter your full name: ")
city = input("Enter your city: ")
language = input("Enter your favorite programming language: ")

# ==========================================
# Display Student Details
# ==========================================

print("\n" + "=" * 50)
print("           STUDENT DETAILS")
print("=" * 50)

print(f"Name               : {name}")
print(f"City               : {city}")
print(f"Favorite Language  : {language}")

print("=" * 50)

# ==========================================
# String Operations
# ==========================================

print("\nString Operations")
print("-" * 50)

print(f"Uppercase          : {name.upper()}")
print(f"Lowercase          : {name.lower()}")
print(f"Title Case         : {name.title()}")

print(f"First Character    : {name[0]}")
print(f"Last Character     : {name[-1]}")

print(f"First 5 Characters : {name[:5]}")
print(f"Reversed Name      : {name[::-1]}")

print(f"Length             : {len(name)}")

print(f"Contains 'a'       : {'a' in name.lower()}")
print(f"Count of 'a'       : {name.lower().count('a')}")

print(f"Replace Spaces     : {name.replace(' ', '_')}")
print(f"Trimmed Name       : {name.strip()}")

print(f"Knows Python       : {language.lower() == 'python'}")

# ==========================================
# Bonus Challenge
# ==========================================

print("\nBonus Challenge")
print("-" * 50)

name_list = name.split()
print(f"Split Name         : {name_list}")

joined_name = "-".join(name_list)
print(f"Joined Name        : {joined_name}")

print(f"Starts with 'T'    : {name.startswith('T')}")
print(f"Ends with 'y'      : {name.endswith('y')}")

# ==========================================
# Program Completed
# ==========================================

print("\n" + "=" * 50)
print("      STRING CHALLENGE COMPLETED!")
print("=" * 50)