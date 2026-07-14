"""
11 - Modules

This file demonstrates how to import and use built-in Python modules.
"""

print("=" * 50)
print("             MODULES")
print("=" * 50)

# ==========================================
# 1. Importing a Module
# ==========================================

print("\n1. Importing a Module")
print("-" * 50)

import math

print("Square Root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)

# ==========================================
# 2. Import Specific Functions
# ==========================================

print("\n2. Import Specific Functions")
print("-" * 50)

from math import sqrt, factorial

print("Square Root of 49:", sqrt(49))
print("Factorial of 5:", factorial(5))

# ==========================================
# 3. Import with Alias
# ==========================================

print("\n3. Import with Alias")
print("-" * 50)

import math as m

print("Value of pi:", m.pi)
print("Power:", m.pow(2, 5))

# ==========================================
# 4. Random Module
# ==========================================

print("\n4. Random Module")
print("-" * 50)

import random

print("Random Integer:", random.randint(1, 10))
print("Random Float:", random.random())

fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Random Choice:", random.choice(fruits))

# ==========================================
# 5. Datetime Module
# ==========================================

print("\n5. Datetime Module")
print("-" * 50)

import datetime

today = datetime.datetime.now()

print("Current Date & Time:", today)
print("Current Date:", today.date())
print("Current Time:", today.time())

# ==========================================
# 6. OS Module
# ==========================================

print("\n6. OS Module")
print("-" * 50)

import os

print("Current Working Directory:")
print(os.getcwd())

# ==========================================
# 7. Sys Module
# ==========================================

print("\n7. Sys Module")
print("-" * 50)

import sys

print("Python Version:")
print(sys.version)

# ==========================================
# 8. Module Information
# ==========================================

print("\n8. Module Information")
print("-" * 50)

print("Math Module Name:", math.__name__)
print("Random Module Name:", random.__name__)

print("\n" + "=" * 50)
print("         MODULES COMPLETED")
print("=" * 50)