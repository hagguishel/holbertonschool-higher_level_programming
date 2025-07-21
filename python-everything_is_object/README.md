# 0x09. Python - Everything is Object

## 📚 Description

This project dives into the core principles of how Python handles memory, variable assignment, object references, mutability, and identity.

Understanding the distinction between **mutable and immutable objects**, **references**, and **aliasing** is essential for writing safe, predictable, and efficient Python code.

You’ll explore how Python behaves under the hood with objects, and you'll be challenged to reason before running any code.

---

## 🧠 Learning Objectives

By the end of this project, you should be able to explain — without Google — the following:

### General Concepts

- What is an object
- Difference between a **class** and an **object (instance)**
- What is a **reference**
- What is an **assignment**
- What is an **alias**
- What is **mutability** and **immutability**
- How to determine if two variables:
  - are identical (`is`)
  - are equal (`==`)
  - reference the same object (`id()`)

### Python Types

- Built-in **mutable** types:
  - `list`
  - `dict`
  - `set`
  - `bytearray`

- Built-in **immutable** types:
  - `int`
  - `float`
  - `str`
  - `tuple`
  - `frozenset`
  - `bytes`

### Functions

- How Python **passes arguments** to functions (by object reference, not value or copy)

---

## 🛠️ Requirements

### Python Scripts

- Files interpreted with Python 3.8.5
- First line: `#!/usr/bin/python3`
- Must end with a new line
- Code must follow **pycodestyle** (version 2.7.*)
- All files must be executable
- Use only allowed functions per task instructions

### Answer Files (`.txt`)

- Contain only **one line** per file
- No space before/after the answer
- No shebang line
- End with a new line

---

## 📎 Resources

- [Objects and Values](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
- [Aliasing](https://docs.python.org/3/glossary.html#term-alias)
- [Mutable vs Immutable Types](https://docs.python.org/3/library/stdtypes.html)
- [Cloning Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Mutation](https://www.geeksforgeeks.org/mutation-python/)
- [Tuples: Immutable but Mutable Inside](https://docs.python.org/3/faq/programming.html#how-can-i-have-an-immutable-object-that-changes-value)

---

## 🧪 Example

```python
a = [1, 2, 3]
b = a
a[0] = 99
print(b)
# Output: [99, 2, 3]  → because lists are mutable and b is an alias of a
