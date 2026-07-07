# 08 - Conditional Statements

## 📖 What are Conditional Statements?

Conditional statements allow a program to make decisions by executing different blocks of code based on whether a condition is **True** or **False**.

Python provides three main conditional statements:

- `if`
- `if...else`
- `if...elif...else`

### Example

```python
age = 18

if age >= 18:
    print("You are eligible to vote.")
```

### Output

```
You are eligible to vote.
```

---

## 🎯 Learning Objectives

After completing this chapter, you will be able to:

- Write `if` statements
- Use `if...else`
- Use `if...elif...else`
- Write nested `if` statements
- Combine conditions using logical operators
- Write concise conditions using the ternary operator

---

## 📚 Topics Covered

- `if` Statement
- `if...else` Statement
- `if...elif...else` Statement
- Nested `if`
- Logical Operators
- Ternary Operator

---

## 🔹 if Statement

Executes a block of code only if the condition is **True**.

### Example

```python
age = 20

if age >= 18:
    print("Adult")
```

Output

```
Adult
```

---

## 🔹 if...else Statement

Executes one block if the condition is **True**, otherwise executes another block.

### Example

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output

```
Minor
```

---

## 🔹 if...elif...else Statement

Used when multiple conditions need to be checked.

### Example

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

Output

```
Grade B
```

---

## 🔹 Nested if

An `if` statement inside another `if` statement.

### Example

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
```

Output

```
Entry Allowed
```

---

## 🔹 Logical Operators

Logical operators combine multiple conditions.

| Operator | Description |
|----------|-------------|
| `and` | True if both conditions are True |
| `or` | True if at least one condition is True |
| `not` | Reverses the result |

### Example

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access Granted")
```

Output

```
Access Granted
```

---

## 🔹 Ternary Operator

A shorter way to write an `if...else` statement.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Example

```python
age = 18

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output

```
Adult
```

---

## 📝 Key Points

- Conditional statements control the flow of a program.
- Conditions evaluate to `True` or `False`.
- Python uses indentation to define code blocks.
- Use `elif` to check multiple conditions.
- Nested `if` statements allow more complex decision-making.
- Ternary operators make simple conditions more concise.

---

## 📂 Files

| File | Description |
|------|-------------|
| `README.md` | Chapter notes |
| `conditional_statements.py` | Examples |
| `practice.py` | Practice exercises |
| `challenge.py` | Challenge program |
| `solution.py` | Challenge solution |

---

## 📚 Next Topic

➡️ Loops