# 03 - Data Types

## 📖 What are Data Types?

A data type defines the type of value a variable can store. Python automatically assigns a data type based on the value assigned to a variable.

### Example

```python
name = "Thulunga"
age = 22
height = 5.8
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

### Output

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

## 🎯 Learning Objectives

After completing this section, you will be able to:

- Understand what data types are.
- Identify different built-in data types in Python.
- Use the `type()` function.
- Use the `isinstance()` function.
- Understand mutable and immutable data types.
- Choose the appropriate data type for different situations.

---

## 📚 Built-in Data Types

### Numeric Types
- `int`
- `float`
- `complex`

### Boolean Type
- `bool`

### Sequence Types
- `str`
- `list`
- `tuple`
- `range`

### Set Types
- `set`
- `frozenset`

### Mapping Type
- `dict`

### Binary Types
- `bytes`
- `bytearray`
- `memoryview`

### None Type
- `NoneType`

---

## 🔄 Mutable vs Immutable

### Mutable Data Types
- List
- Dictionary
- Set
- Bytearray

### Immutable Data Types
- Integer
- Float
- Boolean
- String
- Tuple
- Complex
- Frozenset
- Bytes

---

## 📝 Key Points

- Every value in Python has a data type.
- Python is a dynamically typed language.
- Use `type()` to check the data type of an object.
- Use `isinstance()` to check whether an object belongs to a specific data type.
- Some data types are mutable, while others are immutable.

---

## 📂 Files

| File | Description |
|------|-------------|
| `data_types.py` | Examples of Python data types |
| `practice.py` | Practice questions |
| `challenge.py` | Challenge problem |
| `solution.py` | Challenge solution |

---

## 📚 Next Topic

➡️ Operators