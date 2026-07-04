"""
07 - Strings in Python

This file demonstrates the basics of Python strings.
"""

print("=" * 50)
print("            PYTHON STRINGS")
print("=" * 50)

# ==========================================
# 1. Creating Strings
# ==========================================

print("\n1. Creating Strings")
print("-" * 50)

name = "Thulunga"
language = 'Python'
message = """Welcome to Python"""

print(name)
print(language)
print(message)

# ==========================================
# 2. String Indexing
# ==========================================

print("\n2. String Indexing")
print("-" * 50)

text = "Python"

print(text[0])
print(text[2])
print(text[5])

# ==========================================
# 3. Negative Indexing
# ==========================================

print("\n3. Negative Indexing")
print("-" * 50)

print(text[-1])
print(text[-3])

# ==========================================
# 4. String Slicing
# ==========================================

print("\n4. String Slicing")
print("-" * 50)

print(text[0:4])
print(text[2:])
print(text[:4])
print(text[::2])
print(text[::-1])

# ==========================================
# 5. String Concatenation
# ==========================================

print("\n5. String Concatenation")
print("-" * 50)

first_name = "Thulunga"
last_name = "Narzary"

full_name = first_name + " " + last_name

print(full_name)

# ==========================================
# 6. String Repetition
# ==========================================

print("\n6. String Repetition")
print("-" * 50)

print("Python " * 3)

# ==========================================
# 7. Membership Operators
# ==========================================

print("\n7. Membership Operators")
print("-" * 50)

text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Java" not in text)

# ==========================================
# 8. String Length
# ==========================================

print("\n8. String Length")
print("-" * 50)

print(len(text))

# ==========================================
# 9. Escape Characters
# ==========================================

print("\n9. Escape Characters")
print("-" * 50)

print("Hello\nWorld")
print("Python\tProgramming")
print("He said \"Hello\"")

# ==========================================
# 10. f-Strings
# ==========================================

print("\n10. f-Strings")
print("-" * 50)

name = "Thulunga"
age = 22

print(f"My name is {name}.")
print(f"I am {age} years old.")

# ==========================================
# 11. String Immutability
# ==========================================

print("\n11. String Immutability")
print("-" * 50)

text = "Python"

print(text)

# Strings are immutable.
# Uncommenting the next line will raise an error.

# text[0] = "J"

text = "J" + text[1:]

print(text)

print("\n" + "=" * 50)
print("        STRINGS COMPLETED")
print("=" * 50)