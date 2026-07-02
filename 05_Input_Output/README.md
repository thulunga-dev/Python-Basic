# 05 - Input and Output

## 📖 What is Input and Output?

Input and Output (I/O) allow a program to communicate with the user.

- **Input** is the data entered by the user.
- **Output** is the information displayed by the program.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

- Display output using `print()`
- Accept user input using `input()`
- Convert input into different data types
- Use multiple inputs
- Format output using f-strings
- Customize output using `sep` and `end`
- Use escape characters

---

# 📚 Topics Covered

- print()
- input()
- Type Conversion
- Multiple Inputs
- Formatted Strings (f-strings)
- sep Parameter
- end Parameter
- Escape Characters

---

# 1. The `print()` Function

The `print()` function is used to display output on the screen.

### Example

```python
print("Hello, World!")
```

### Output

```
Hello, World!
```

---

# 2. The `input()` Function

The `input()` function accepts input from the user.

### Example

```python
name = input("Enter your name: ")

print(name)
```

### Output

```
Enter your name: Thulunga
Thulunga
```

> **Note:** `input()` always returns a string.

---

# 3. Type Conversion

Convert user input into another data type.

### Example

```python
age = int(input("Enter your age: "))

print(age)
```

### Output

```
Enter your age: 22
22
```

---

# 4. Multiple Inputs

You can take multiple inputs.

### Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(name, age)
```

### Output

```
Enter your name: Thulunga
Enter your age: 22

Thulunga 22
```

---

# 5. Formatted Strings (f-strings)

f-strings make printing variables easier.

### Example

```python
name = "Thulunga"
age = 22

print(f"My name is {name}.")
print(f"I am {age} years old.")
```

### Output

```
My name is Thulunga.
I am 22 years old.
```

---

# 6. The `sep` Parameter

The `sep` parameter changes the separator between values.

### Example

```python
print("Python", "Java", "C++", sep=" | ")
```

### Output

```
Python | Java | C++
```

---

# 7. The `end` Parameter

The `end` parameter changes what is printed at the end of a `print()` statement.

### Example

```python
print("Hello", end=" ")
print("World")
```

### Output

```
Hello World
```

---

# 8. Escape Characters

Escape characters are used to format strings.

### Example

```python
print("Hello\nWorld")
print("Python\tProgramming")
print("He said \"Hello\"")
```

### Output

```
Hello
World

Python    Programming

He said "Hello"
```

---

# 📝 Key Points

- `print()` displays output.
- `input()` accepts user input.
- `input()` always returns a string.
- Use `int()`, `float()`, etc. for type conversion.
- Use f-strings for readable output.
- `sep` changes the separator.
- `end` changes the line ending.
- Escape characters improve text formatting.

---

# 📂 Files

| File | Description |
|------|-------------|
| `input_output.py` | Examples of input and output |
| `practice.py` | Practice exercises |
| `challenge.py` | Challenge problem |
| `solution.py` | Challenge solution |

---

# 📚 Next Topic

➡️ Type Casting