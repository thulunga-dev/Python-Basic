"""
07 - Strings Practice
"""

print("=" * 50)
print("          STRING PRACTICE")
print("=" * 50)

# ==========================================
# Practice 1: Create a String
# ==========================================

name = "Thulunga"

print("1. Create a String")
print(name)

# ==========================================
# Practice 2: String Indexing
# ==========================================

print("\n2. String Indexing")

text = "Python"

print(text[0])
print(text[2])
print(text[5])

# ==========================================
# Practice 3: Negative Indexing
# ==========================================

print("\n3. Negative Indexing")

print(text[-1])
print(text[-3])

# ==========================================
# Practice 4: String Slicing
# ==========================================

print("\n4. String Slicing")

print(text[0:4])
print(text[2:])
print(text[:4])
print(text[::-1])

# ==========================================
# Practice 5: String Concatenation
# ==========================================

print("\n5. String Concatenation")

first_name = "Thulunga"
last_name = "Narzary"

print(first_name + " " + last_name)

# ==========================================
# Practice 6: String Repetition
# ==========================================

print("\n6. String Repetition")

print("Python " * 3)

# ==========================================
# Practice 7: Membership Operators
# ==========================================

print("\n7. Membership Operators")

language = "Python Programming"

print("Python" in language)
print("Java" in language)
print("Java" not in language)

# ==========================================
# Practice 8: String Length
# ==========================================

print("\n8. String Length")

print(len(language))

# ==========================================
# Practice 9: String Methods
# ==========================================

print("\n9. String Methods")

text = " python programming "

print(text.upper())
print(text.lower())
print(text.title())
print(text.strip())
print(text.replace("python", "Java"))
print(text.count("p"))
print(text.find("programming"))

# ==========================================
# Practice 10: Split and Join
# ==========================================

print("\n10. Split and Join")

languages = "Python Java C++"

language_list = languages.split()

print(language_list)

print(", ".join(language_list))

# ==========================================
# Practice 11: Escape Characters
# ==========================================

print("\n11. Escape Characters")

print("Hello\nWorld")
print("Python\tProgramming")
print("He said \"Hello\"")

# ==========================================
# Practice 12: f-Strings
# ==========================================

print("\n12. f-Strings")

name = "Thulunga"
age = 22

print(f"My name is {name}.")
print(f"I am {age} years old.")

print("\n" + "=" * 50)
print("      STRING PRACTICE COMPLETED")
print("=" * 50)