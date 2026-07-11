"""
10 - Recursion

This file demonstrates recursive functions in Python.
"""

print("=" * 50)
print("            RECURSION")
print("=" * 50)

# ==========================================
# 1. Basic Recursion
# ==========================================

print("\n1. Basic Recursion")
print("-" * 50)

def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)

countdown(5)

# ==========================================
# 2. Factorial
# ==========================================

print("\n2. Factorial")
print("-" * 50)

def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)

print(f"5! = {factorial(5)}")

# ==========================================
# 3. Sum of Natural Numbers
# ==========================================

print("\n3. Sum of Natural Numbers")
print("-" * 50)

def sum_numbers(number):
    if number == 1:
        return 1

    return number + sum_numbers(number - 1)

print(sum_numbers(10))

# ==========================================
# 4. Fibonacci Series
# ==========================================

print("\n4. Fibonacci Series")
print("-" * 50)

def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)

for i in range(10):
    print(fibonacci(i), end=" ")

print()

# ==========================================
# 5. Power of a Number
# ==========================================

print("\n5. Power of a Number")
print("-" * 50)

def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print(power(2, 5))

# ==========================================
# 6. Reverse a String
# ==========================================

print("\n6. Reverse a String")
print("-" * 50)

def reverse_string(text):
    if len(text) == 0:
        return ""

    return text[-1] + reverse_string(text[:-1])

print(reverse_string("Python"))

# ==========================================
# 7. Count Digits
# ==========================================

print("\n7. Count Digits")
print("-" * 50)

def count_digits(number):
    if number < 10:
        return 1

    return 1 + count_digits(number // 10)

print(count_digits(123456))

# ==========================================
# 8. Print Numbers (Ascending)
# ==========================================

print("\n8. Print Numbers (Ascending)")
print("-" * 50)

def ascending(number):
    if number == 0:
        return

    ascending(number - 1)
    print(number)

ascending(5)

# ==========================================
# 9. Print Numbers (Descending)
# ==========================================

print("\n9. Print Numbers (Descending)")
print("-" * 50)

def descending(number):
    if number == 0:
        return

    print(number)
    descending(number - 1)

descending(5)

# ==========================================
# 10. Recursion vs Loop
# ==========================================

print("\n10. Recursion vs Loop")
print("-" * 50)

print("Loop:")

for i in range(1, 6):
    print(i)

print("\nRecursion:")

def print_numbers(number):
    if number == 6:
        return

    print(number)
    print_numbers(number + 1)

print_numbers(1)

print("\n" + "=" * 50)
print("       RECURSION COMPLETED")
print("=" * 50)