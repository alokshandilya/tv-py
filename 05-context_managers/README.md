# Table of Contents

1. [Basic Understanding of Context Managers](#1-basic-understanding-of-context-managers)
   - [What is a Context Manager?](#what-is-a-context-manager)
   - [Syntax](#syntax)
   - [Example: Using a Built-in Context Manager](#example-using-a-built-in-context-manager)

2. [Custom Context Managers](#2-custom-context-managers)
   - [Simple Custom Context Manager](#a-simple-custom-context-manager)
   - [Managing Resources](#b-managing-resources)

3. [Context Managers with `contextlib`](#3-context-managers-with-contextlib)
   - [Using `@contextmanager`](#a-using-contextmanager)
   - [Nested Context Managers](#b-nested-context-managers)

4. [Advanced Concepts](#4-advanced-concepts)
   - [Exception Handling](#a-exception-handling)
   - [Dynamic Context Managers](#b-dynamic-context-managers)

5. [Best Practices](#5-best-practices)

6. [Practical Use Cases](#6-practical-use-cases)
   - [File Handling](#a-file-handling)
   - [Database Connections](#b-database-connections)
   - [Temporary Directories](#c-temporary-directories)
   - [Timing Blocks](#d-timing-blocks)

7. [Context Managers vs Decorators](#7-context-managers-vs-decorators)

# Context Managers

- a powerful tool for managing resources, such as file handling, database connections, or any scenario where you need to ensure proper setup and cleanup of resources.
- help avoiding common pitfalls like resource leaks by ensuring that resources are properly released, even if an error occurs.

## 1. Basic Understanding of Context Managers

### What is a Context Manager?

A context manager is an object that defines the methods `__enter__()` and `__exit__()`. These methods are used to set up and tear down resources, respectively. The `with` statement is used to invoke a context manager.

- `__enter__()`: Called when entering the `with` block. It can return a value that is assigned to the variable after `as`.
- `__exit__()`: Called when exiting the `with` block. It handles cleanup, such as closing files or releasing locks.

### Syntax

```python
with context_manager as resource:
    # Use the resource here
```

#### Example: Using a Built-in Context Manager

The `open()` function is a built-in context manager for file handling:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed when the block exits
```

## 2. Custom Context Managers

You can create your own context managers by defining a class that implements `__enter__()` and `__exit__()`.

### a. Simple Custom Context Manager

Here’s an example of a custom context manager that prints messages when entering and exiting:

```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self  # Optional: Return an object to be used inside the block

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return False  # Propagate exceptions (True suppresses them)

with MyContextManager() as cm:
    print("Inside the context")
```

**Output:**

```
Entering the context
Inside the context
Exiting the context
```

If an exception occurs:

```python
with MyContextManager() as cm:
    raise ValueError("Something went wrong!")
```

**Output:**

```
Entering the context
Exiting the context
An exception occurred: Something went wrong!
Traceback (most recent call last):
...
ValueError: Something went wrong!
```

### b. Managing Resources

A custom context manager can manage resources like database connections or locks.

#### Example: Lock Management

```python
import threading

class LockManager:
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        self.lock.acquire()
        print("Lock acquired")
        return self.lock

    def __exit__(self, exc_type, exc_value, traceback):
        self.lock.release()
        print("Lock released")

lock_manager = LockManager()
with lock_manager as lock:
    print("Critical section")
```

**Output:**

```
Lock acquired
Critical section
Lock released
```

## 3. Context Managers with `contextlib`

Python provides the `contextlib` module, which simplifies the creation of context managers using decorators or helper functions.

### a. Using `@contextmanager`

The `@contextmanager` decorator allows you to define context managers as generator functions.

#### Example: File Handling

```python
from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    file = open(file_name, mode)
    try:
        print("Opening file")
        yield file
    finally:
        print("Closing file")
        file.close()

with open_file('example.txt', 'r') as file:
    print(file.read())
```

**Output:**

```
Opening file
<file content>
Closing file
```

### b. Nested Context Managers

You can combine multiple context managers using `contextlib.ExitStack`.

#### Example: Multiple Files

```python
from contextlib import ExitStack

file_names = ['file1.txt', 'file2.txt', 'file3.txt']
with ExitStack() as stack:
    files = [stack.enter_context(open(fname, 'r')) for fname in file_names]
    for file in files:
        print(file.read())
```

## 4. Advanced Concepts

### a. Exception Handling

The `__exit__()` method receives details about any exception that occurred (`exc_type`, `exc_value`, `traceback`). You can handle or suppress exceptions by returning `True` from `__exit__()`.

#### Example: Suppressing Exceptions

```python
class SuppressErrors:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Suppressing exception: {exc_value}")
        return True  # Suppress the exception

with SuppressErrors():
    raise ValueError("This will be suppressed")
```

**Output:**

```
Suppressing exception: This will be suppressed
```

### b. Dynamic Context Managers

You can dynamically create context managers based on runtime conditions.

#### Example: Conditional Resource Allocation

```python
class ConditionalManager:
    def __init__(self, condition):
        self.condition = condition

    def __enter__(self):
        if self.condition:
            print("Condition met, allocating resource")
        else:
            print("Condition not met, skipping allocation")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.condition:
            print("Releasing resource")

with ConditionalManager(True) as cm:
    print("Inside the context")
```

**Output:**

```
Condition met, allocating resource
Inside the context
Releasing resource
```

## 5. Best Practices

1. **Use `with` Statements:** Always use `with` statements for resource management to ensure proper cleanup.
2. **Handle Exceptions Gracefully:** Decide whether to suppress or propagate exceptions in `__exit__()`.
3. **Keep Context Managers Focused:** Each context manager should manage a single resource or responsibility.
4. **Leverage `contextlib`:** Use `contextlib` for simpler implementations instead of defining full classes.
5. **Document Behavior:** Clearly document what the context manager does, its inputs, and its behavior during exceptions.

## 6. Practical Use Cases

### a. File Handling

Ensure files are properly closed after reading or writing:

```python
with open('data.txt', 'r') as file:
    data = file.read()
```

### b. Database Connections

Manage database connections and transactions:

```python
class DatabaseConnection:
    def __enter__(self):
        self.connection = connect_to_database()
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

with DatabaseConnection() as db:
    execute_query(db, "SELECT * FROM users")
```

### c. Temporary Directories

Create and clean up temporary directories:

```python
import tempfile
import shutil

@contextmanager
def temp_directory():
    dir_path = tempfile.mkdtemp()
    try:
        print(f"Created directory: {dir_path}")
        yield dir_path
    finally:
        print(f"Deleting directory: {dir_path}")
        shutil.rmtree(dir_path)

with temp_directory() as tmp_dir:
    print(f"Using directory: {tmp_dir}")
```

### d. Timing Blocks

Measure the execution time of a block of code:

```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time:.4f} seconds")

with timer():
    time.sleep(2)
```

**Output:**

```
Elapsed time: 2.0002 seconds
```

## 7. Context Managers vs Decorators

| Feature        | Context Manager                  | Decorator                          |
| -------------- | -------------------------------- | ---------------------------------- |
| Purpose        | Manage resources (setup/cleanup) | Modify or extend function behavior |
| Scope          | Block-level                      | Function-level                     |
| Implementation | Requires `__enter__`/`__exit__`  | Defined as a function              |
| Use Case       | File handling, locks, etc.       | Logging, caching, validation, etc. |

---

- with mastering context managers, can write robust, clean, and maintainable code that **ensures proper resource management**.
  - particularly valuable for scenarios involving **file I/O, database connections, threading**, and more.
