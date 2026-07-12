# 10 - Functions

## 📖 What are Functions?

A **function** is a reusable block of code that performs a specific task. Functions help reduce code duplication, improve readability, and make programs easier to maintain.

Python provides many built-in functions like `print()` and `len()`, and also allows you to create your own functions using the `def` keyword.

### Example

```python
def greet():
    print("Hello, World!")

greet()
```

### Output

```
Hello, World!
```

---

## 🎯 Learning Objectives

After completing this chapter, you will be able to:

- Define and call functions
- Pass arguments to functions
- Return values from functions
- Use different types of function arguments
- Understand local and global scope
- Create lambda functions
- Write recursive functions

---

## 📚 Topics Covered

- Defining Functions
- Calling Functions
- Parameters and Arguments
- Return Statement
- Default Arguments
- Keyword Arguments
- `*args`
- `**kwargs`
- Variable Scope
- Lambda Functions
- Recursion

---

## 🔹 Defining a Function

```python
def greet():
    print("Hello!")
```

---

## 🔹 Function with Parameters

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
```

---

## 🔹 Return Statement

```python
def add(a, b):
    return a + b

print(add(5, 3))
```

Output

```
8
```

---

## 🔹 Default Arguments

```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Alice")
```

---

## 🔹 *args

Accepts any number of positional arguments.

```python
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30)
```

---

## 🔹 **kwargs

Accepts any number of keyword arguments.

```python
def student(**details):
    print(details)

student(name="John", age=22)
```

---

## 🔹 Lambda Function

```python
square = lambda x: x ** 2

print(square(5))
```

Output

```
25
```

---

## 🔹 Recursion

A recursive function calls itself until a base case is reached.

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)
```

---

## 📝 Key Points

- Functions make code reusable.
- Functions can accept parameters and return values.
- `*args` accepts multiple positional arguments.
- `**kwargs` accepts multiple keyword arguments.
- Lambda functions are anonymous functions.
- Recursive functions call themselves.
- Every recursive function must have a base case.

---

## 📂 Files

| File | Description |
|------|-------------|
| `README.md` | Chapter notes |
| `functions.py` | Basic function examples |
| `function_arguments.py` | Parameters, arguments, `*args`, `**kwargs` |
| `lambda_functions.py` | Lambda function examples |
| `recursion.py` | Recursive function examples |
| `practice.py` | Practice exercises |
| `challenge.py` | Challenge program |
| `solution.py` | Challenge solution |

---

