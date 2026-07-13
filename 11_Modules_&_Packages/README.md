# 11 - Modules and Packages

## 📖 What are Modules and Packages?

A **module** is a Python file (`.py`) that contains functions, variables, or classes that can be reused in other programs.

A **package** is a collection of related Python modules organized inside a folder.

Using modules and packages helps organize code, improve reusability, and make large projects easier to maintain.

---

## 🎯 Learning Objectives

After completing this chapter, you will be able to:

- Understand modules and packages
- Import built-in modules
- Create your own modules
- Import functions from modules
- Use aliases with modules
- Understand packages and `__init__.py`
- Use the `__name__` variable

---

## 📚 Topics Covered

- Modules
- Built-in Modules
- Import Statement
- `from ... import ...`
- Module Aliases
- Custom Modules
- Packages
- `__init__.py`
- `__name__`
- `if __name__ == "__main__"`

---

## 🔹 Importing a Module

```python
import math

print(math.sqrt(25))
```

Output

```
5.0
```

---

## 🔹 Importing Specific Functions

```python
from math import sqrt

print(sqrt(49))
```

Output

```
7.0
```

---

## 🔹 Import with Alias

```python
import math as m

print(m.pi)
```

Output

```
3.141592653589793
```

---

## 🔹 Custom Module

```python
# greetings.py

def hello():
    print("Hello, Python!")
```

```python
import greetings

greetings.hello()
```

Output

```
Hello, Python!
```

---

## 🔹 Packages

A package is a folder that contains one or more Python modules.

Example:

```
my_package/
│
├── __init__.py
├── module1.py
└── module2.py
```

---

## 🔹 __name__ Variable

Every Python file has a special variable called `__name__`.

```python
if __name__ == "__main__":
    print("Executed directly")
```

This code runs only when the file is executed directly, not when it is imported.

---

## 📝 Key Points

- A module is a Python file.
- A package is a collection of modules.
- Use `import` to reuse code.
- `from ... import ...` imports specific objects.
- Use `as` to create aliases.
- `__init__.py` identifies a package.
- `__name__ == "__main__"` controls program execution.

---

## 📂 Files

| File | Description |
|------|-------------|
| `README.md` | Chapter notes |
| `modules.py` | Built-in module examples |
| `custom_module.py` | Creating and using custom modules |
| `packages.py` | Creating and importing packages |
| `practice.py` | Practice exercises |
| `challenge.py` | Challenge program |
| `solution.py` | Challenge solution |

---