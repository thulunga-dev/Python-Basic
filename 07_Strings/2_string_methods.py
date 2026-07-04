"""
07 - String Methods

This file demonstrates commonly used string methods in Python.
"""

print("=" * 50)
print("         STRING METHODS")
print("=" * 50)

# ==========================================
# 1. upper()
# ==========================================

text = "python"
print("\n1. upper()")
print(text.upper())

# ==========================================
# 2. lower()
# ==========================================

text = "PYTHON"
print("\n2. lower()")
print(text.lower())

# ==========================================
# 3. capitalize()
# ==========================================

text = "python programming"
print("\n3. capitalize()")
print(text.capitalize())

# ==========================================
# 4. title()
# ==========================================

text = "python programming"
print("\n4. title()")
print(text.title())

# ==========================================
# 5. swapcase()
# ==========================================

text = "PyThOn"
print("\n5. swapcase()")
print(text.swapcase())

# ==========================================
# 6. strip()
# ==========================================

text = "   Python   "
print("\n6. strip()")
print(text.strip())

# ==========================================
# 7. lstrip()
# ==========================================

text = "   Python"
print("\n7. lstrip()")
print(text.lstrip())

# ==========================================
# 8. rstrip()
# ==========================================

text = "Python   "
print("\n8. rstrip()")
print(text.rstrip())

# ==========================================
# 9. replace()
# ==========================================

text = "Hello World"
print("\n9. replace()")
print(text.replace("World", "Python"))

# ==========================================
# 10. find()
# ==========================================

text = "Python Programming"
print("\n10. find()")
print(text.find("Programming"))

# ==========================================
# 11. index()
# ==========================================

text = "Python"
print("\n11. index()")
print(text.index("t"))

# ==========================================
# 12. count()
# ==========================================

text = "banana"
print("\n12. count()")
print(text.count("a"))

# ==========================================
# 13. startswith()
# ==========================================

text = "Python"
print("\n13. startswith()")
print(text.startswith("Py"))

# ==========================================
# 14. endswith()
# ==========================================

text = "Python"
print("\n14. endswith()")
print(text.endswith("on"))

# ==========================================
# 15. split()
# ==========================================

text = "Python Java C++"
print("\n15. split()")
print(text.split())

# ==========================================
# 16. join()
# ==========================================

languages = ["Python", "Java", "C++"]
print("\n16. join()")
print(", ".join(languages))

# ==========================================
# 17. isalpha()
# ==========================================

text = "Python"
print("\n17. isalpha()")
print(text.isalpha())

# ==========================================
# 18. isdigit()
# ==========================================

text = "12345"
print("\n18. isdigit()")
print(text.isdigit())

# ==========================================
# 19. isalnum()
# ==========================================

text = "Python123"
print("\n19. isalnum()")
print(text.isalnum())

# ==========================================
# 20. isspace()
# ==========================================

text = "   "
print("\n20. isspace()")
print(text.isspace())

# ==========================================
# 21. center()
# ==========================================

text = "Python"
print("\n21. center()")
print(text.center(20, "-"))

# ==========================================
# 22. ljust()
# ==========================================

text = "Python"
print("\n22. ljust()")
print(text.ljust(15, "-"))

# ==========================================
# 23. rjust()
# ==========================================

text = "Python"
print("\n23. rjust()")
print(text.rjust(15, "-"))

# ==========================================
# 24. zfill()
# ==========================================

text = "25"
print("\n24. zfill()")
print(text.zfill(5))

print("\n" + "=" * 50)
print("     STRING METHODS COMPLETED")
print("=" * 50)