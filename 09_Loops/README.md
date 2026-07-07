# 09 - Loops

## 📖 What are Loops?

Loops allow you to execute a block of code repeatedly until a condition is met or a sequence is exhausted.

Python provides two types of loops:

- `for` loop
- `while` loop

Loops help reduce code repetition and make programs more efficient.

### Example

```python
for i in range(5):
    print(i)
```

### Output

```
0
1
2
3
4
```

---

## 🎯 Learning Objectives

After completing this chapter, you will be able to:

- Understand loops
- Use `for` loops
- Use `while` loops
- Generate sequences using `range()`
- Control loops using `break`, `continue`, and `pass`
- Write nested loops
- Solve pattern-based problems

---

## 📚 Topics Covered

- `for` Loop
- `while` Loop
- `range()` Function
- Nested Loops
- `break` Statement
- `continue` Statement
- `pass` Statement

---

## 🔹 for Loop

A `for` loop is used to iterate over a sequence such as a string, list, tuple, set, dictionary, or range.

### Syntax

```python
for variable in sequence:
    # code
```

### Example

```python
for fruit in ["Apple", "Banana", "Mango"]:
    print(fruit)
```

Output

```
Apple
Banana
Mango
```

---

## 🔹 while Loop

A `while` loop executes as long as the condition remains `True`.

### Syntax

```python
while condition:
    # code
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```
1
2
3
4
5
```

---

## 🔹 range() Function

The `range()` function generates a sequence of numbers.

### Syntax

```python
range(start, stop, step)
```

### Examples

```python
range(5)
range(1, 6)
range(1, 10, 2)
```

---

## 🔹 Nested Loops

A loop inside another loop is called a nested loop.

### Example

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Output

```
0 0
0 1
1 0
1 1
2 0
2 1
```

---

## 🔹 break Statement

Stops the loop immediately.

### Example

```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
```

Output

```
1
2
3
```

---

## 🔹 continue Statement

Skips the current iteration and moves to the next one.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output

```
1
2
4
5
```

---

## 🔹 pass Statement

The `pass` statement does nothing. It is used as a placeholder for future code.

### Example

```python
for i in range(5):
    if i == 3:
        pass
    print(i)
```

Output

```
0
1
2
3
4
```

---

## 📝 Key Points

- Use `for` loops when the number of iterations is known.
- Use `while` loops when the number of iterations depends on a condition.
- `range()` generates sequences of numbers.
- `break` exits a loop.
- `continue` skips the current iteration.
- `pass` acts as a placeholder.
- Nested loops are useful for working with tables and patterns.

---

## 📂 Files

| File | Description |
|------|-------------|
| `README.md` | Chapter notes |
| `for_loop.py` | Examples of for loops |
| `while_loop.py` | Examples of while loops |
| `loop_control.py` | break, continue, and pass |
| `practice.py` | Practice exercises |
| `challenge.py` | Challenge programs |
| `solution.py` | Challenge solutions |

---

