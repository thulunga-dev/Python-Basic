# 10 - Functions

## 📖 What are Functions?

A **function** is a reusable block of code that performs a specific task. Functions help make programs organized, reusable, and easier to maintain.

Python provides built-in functions like `print()` and `len()`, and also allows you to create your own functions using the `def` keyword.

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
- Use parameters and arguments
- Return values from functions
- Work with default parameters
- Use keyword arguments
- Use `*args` and `**kwargs`
- Understand variable scope
- Create lambda functions
- Write basic recursive functions

---

## 📚 Topics Covered

- Defining Functions
- Calling Functions
- Parameters
- Arguments
- Return Statement
- Default Parameters
- Keyword Arguments
- Variable-Length Arguments (`*args`)
- Keyword Variable Arguments (`**kwargs`)
- Variable Scope
- Lambda Functions
- Recursion

---

## 🔹 Defining a Function

Functions are defined using the `def` keyword.

### Example

```python
def greet():
    print("Hello!")
```

---

## 🔹 Calling a Function

Call a function using its name followed by parentheses.

### Example

```python
greet()
```

Output

```
Hello!
```

---

## 🔹 Parameters and Arguments

Parameters receive values passed to a function.

### Example

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
```

Output

```
Hello, Alice
```

---

## 🔹 Return Statement

The `return` statement sends a value back to the caller.

### Example

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

Output

```
8
```

---

## 🔹 Default Parameters

A default value is used if no argument is provided.

### Example

```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Alice")
```

Output

```
Hello, Guest
Hello, Alice
```

---

## 🔹 Variable-Length Arguments

### `*args`

Accepts multiple positional arguments.

```python
def total(*numbers):
    print(sum(numbers))
```

### `**kwargs`

Accepts multiple keyword arguments.

```python
def student(**details):
    print(details)
```

---

## 🔹 Variable Scope

- **Local Variable:** Exists only inside a function.
- **Global Variable:** Can be accessed throughout the program.

### Example

```python
message = "Python"

def show():
    print(message)

show()
```

---

## 🔹 Lambda Functions

A lambda function is a small anonymous function.

### Example

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

A recursive function calls itself until a stopping condition is met.

### Example

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

Output

```
5
4
3
2
1
```

---

## 📝 Key Points

- Functions make code reusable.
- Use `def` to create a function.
- Functions can accept parameters and return values.
- `*args` accepts multiple positional arguments.
- `**kwargs` accepts multiple keyword arguments.
- Variables can have local or global scope.
- Lambda functions are useful for short operations.
- Recursion requires a base case to avoid infinite calls.

---

## 📂 Files

| File | Description |
|------|-------------|
| `README.md` | Chapter notes |
| `functions.py` | Function examples |
| `practice.py` | Practice exercises |
| `challenge.py` | Challenge program |
| `solution.py` | Challenge solution |

---
