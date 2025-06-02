# 📁 0x0B. Python - Input/Output

## 📚 Description

This project dives into file handling and data serialization in Python. It covers reading from and writing to files, working with the `with` statement, understanding JSON, and managing command-line arguments via the `sys` module.

By the end of the project, you’ll have a strong foundation in file operations and data serialization — essential skills for real-world Python scripting and automation.

## 🧠 Learning Objectives

You should be able to explain the following concepts without relying on Google:

### General

- Why Python is awesome.
- How to open and close a file properly.
- How to write text into a file.
- How to read the entire content of a file.
- How to read a file line by line.
- How to move the file cursor (`seek()` and `tell()`).
- Why and how to use the `with` statement for clean file handling.
- What JSON is and how it works.
- What serialization and deserialization mean.
- How to convert a Python data structure to a JSON string.
- How to convert a JSON string back into a Python object.
- How to access and use command-line arguments using `sys.argv`.

## 📖 Resources

- [Python Docs: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Dive Into Python 3 – Chapter 11: Files (until 11.4)](https://diveintopython3.problemsolving.io/files.html)
- [Python JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Automate the Boring Stuff – Chapter 8 & 14](https://automatetheboringstuff.com)
- [Learn to Program – Chapter 8](https://greenteapress.com/thinkpython2/html/thinkpython2009.html)
- [Python sys package](https://docs.python.org/3/library/sys.html)

## 🧪 Project Requirements

### ✅ Python Scripts

- Language: Python 3.8.5
- Files must start with: `#!/usr/bin/python3`
- Must follow **pycodestyle** (version 2.7.\*)
- Each file must end with a newline
- All files must be executable
- Each file’s length will be tested using `wc`
- A `README.md` file is mandatory

### 🧪 Python Test Cases

- Editors allowed: `vi`, `vim`, `emacs`
- All test files are located in the `tests/` folder
- Test file extension: `.txt`
- Tests run using: `python3 -m doctest ./tests/*`

### 📑 Documentation

Every:
- **Module**
- **Class**
- **Function**

…must have a docstring that:
- Is a **full sentence** describing its purpose
- Can be checked with:
  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
  python3 -c 'print(__import__("my_module").MyClass.__doc__)'
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
