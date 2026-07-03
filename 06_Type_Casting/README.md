# 06 - Type Casting

## 📖 What is Type Casting?

Type casting is the process of converting a value from one data type to another.

Python provides built-in functions to perform type conversion.

### Example

```python
age = "22"

age = int(age)

print(age)
print(type(age))
```

### Output

```
22
<class 'int'>
```

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

- Understand type casting.
- Convert one data type to another.
- Perform implicit type conversion.
- Perform explicit type conversion.
- Use Python's built-in conversion functions.

---

# 📚 Topics Covered

- What is Type Casting?
- Implicit Type Casting
- Explicit Type Casting
- int()
- float()
- str()
- bool()
- list()
- tuple()
- set()
- dict()

---

# 1. Implicit Type Casting

Python automatically converts one data type into another.

### Example

```python
x = 10
y = 5.5

print(x + y)
```

### Output

```
15.5
```

---

# 2. Explicit Type Casting

The programmer manually converts a data type.

### Example

```python
age = "22"

age = int(age)

print(age)
```

---

# 3. int()

Converts a value to an integer.

```python
print(int(5.9))
```

Output

```
5
```

---

# 4. float()

Converts a value to a float.

```python
print(float(10))
```

Output

```
10.0
```

---

# 5. str()

Converts a value to a string.

```python
print(str(100))
```

Output

```
100
```

---

# 6. bool()

Converts a value to Boolean.

```python
print(bool(1))
print(bool(0))
```

Output

```
True
False
```

---

# 7. list()

```python
numbers = (1, 2, 3)

print(list(numbers))
```

---

# 8. tuple()

```python
numbers = [1, 2, 3]

print(tuple(numbers))
```

---

# 9. set()

```python
numbers = [1, 2, 2, 3]

print(set(numbers))
```

---

## 📝 Key Points

- Python supports implicit and explicit type casting.
- Use built-in conversion functions.
- Not every conversion is valid.
- Be careful while converting strings into numbers.

---

## 📂 Files

| File | Description |
|------|-------------|
| `type_casting.py` | Type casting examples |
| `practice.py` | Practice exercises |
| `challenge.py` | Challenge problem |
| `solution.py` | Challenge solution |

---

## 📚 Next Topic

➡️ Strings