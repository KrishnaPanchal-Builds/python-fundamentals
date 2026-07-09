# 🔁 Module 04 - Loops

> Python Fundamentals Repository

Loops are one of the most fundamental concepts in programming. They allow a program to execute a block of code repeatedly until a specified condition is met.

Without loops, programmers would have to write the same code multiple times, making programs lengthy, repetitive, and difficult to maintain.

Loops are widely used in almost every software application, including web applications, mobile apps, games, automation scripts, artificial intelligence, data analysis, and enterprise software.

---

# 🎯 Learning Objectives

After completing this module, you will be able to:

- ✅ Understand why loops are used.
- ✅ Use the `for` loop.
- ✅ Use the `while` loop.
- ✅ Work with nested loops.
- ✅ Control loop execution using `break`.
- ✅ Skip iterations using `continue`.
- ✅ Understand the purpose of `pass`.
- ✅ Build real-world applications using loops.

---

# 📚 Topics Covered

| Topic | Description |
|--------|-------------|
| `for` Loop | Repeats a block of code for every item in a sequence. |
| `while` Loop | Repeats a block of code until a condition becomes false. |
| Nested Loops | A loop inside another loop. |
| `break` Statement | Terminates a loop immediately. |
| `continue` Statement | Skips the current iteration and moves to the next one. |
| `pass` Statement | Placeholder for future code. |

---

# 🤔 What is a Loop?

A loop is a programming construct that executes a block of code repeatedly.

Instead of writing the same statements multiple times, a loop performs the repetition automatically.

Example:

- Sending notifications to multiple users.
- Displaying products in an online store.
- Processing student records.
- Reading data from a file.
- Repeating a task until the user exits.

---

# 🔹 For Loop

The `for` loop is used when the number of iterations is known or when iterating through a sequence such as a string, list, tuple, set, dictionary, or range.

### Syntax

```python
for variable in sequence:
    statement
```

### Example

```python
for number in range(1, 6):
    print(number)
```

---

# 🔹 While Loop

The `while` loop executes as long as a specified condition remains `True`.

### Syntax

```python
while condition:
    statement
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# 🔹 Nested Loops

A nested loop is a loop placed inside another loop.

Nested loops are commonly used for working with tables, matrices, patterns, grids, and multi-level data.

### Example

```python
for row in range(3):
    for column in range(3):
        print("*", end=" ")
    print()
```

---

# 🔹 Break Statement

The `break` statement immediately terminates the current loop.

### Example

```python
for number in range(10):

    if number == 5:
        break

    print(number)
```

---

# 🔹 Continue Statement

The `continue` statement skips the current iteration and proceeds to the next iteration of the loop.

### Example

```python
for number in range(6):

    if number == 3:
        continue

    print(number)
```

---

# 🔹 Pass Statement

The `pass` statement performs no action.

It acts as a placeholder for code that will be implemented later.

### Example

```python
for number in range(5):

    if number == 3:
        pass

    print(number)
```

---

# 🌍 Real-World Applications

Loops are used extensively in:

- 🛒 E-Commerce Applications
- 🏦 Banking Systems
- 📚 Library Management Systems
- 🎓 Student Management Systems
- 📊 Data Analysis
- 🤖 Artificial Intelligence
- 🌐 Web Applications
- 📱 Mobile Applications
- 🎮 Game Development
- 🤖 Automation Scripts

---

# 💼 Practical Application

## E-Commerce Shopping System

In this module, you will build an interactive shopping system that demonstrates the practical use of loops.

The application will:

- Display product categories.
- Show products using loops.
- Allow continuous shopping.
- Handle menu-driven navigation.
- Generate a shopping summary.
- Demonstrate `for`, `while`, nested loops, `break`, and `continue` naturally.

---

# 🎓 Learning Outcomes

After completing this module, you will be able to:

- ✔️ Write efficient looping logic.
- ✔️ Eliminate repetitive code.
- ✔️ Build menu-driven applications.
- ✔️ Process collections of data.
- ✔️ Control loop execution using `break` and `continue`.
- ✔️ Apply loops confidently in real-world projects.

---

# 📌 Key Takeaways

- Loops eliminate repetitive code.
- `for` loops iterate over sequences.
- `while` loops repeat until a condition changes.
- Nested loops handle multi-level repetition.
- `break` exits a loop immediately.
- `continue` skips the current iteration.
- `pass` acts as a placeholder for future implementation.

---

<div align="center">

# 🎉 Module Complete!

You have learned how loops automate repetitive tasks and form the backbone of countless real-world applications.

**Happy Coding! 🐍🚀**

</div>
