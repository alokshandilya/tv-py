# Table of Contents

1. [Basic Understanding of Scopes](#1-basic-understanding-of-scopes)
    - [What is Scope?](#what-is-scope)
    - [Types of Scopes](#types-of-scopes)
2. [Types of Scopes in Detail](#2-types-of-scopes-in-detail)
    - [Local Scope](#a-local-scope)
        - [Example: Local Scope](#example-local-scope)
    - [Enclosing (Nonlocal) Scope](#b-enclosing-nonlocal-scope)
        - [Example: Enclosing Scope](#example-enclosing-scope)
        - [Example: Modifying Enclosing Variables](#example-modifying-enclosing-variables)
    - [Global Scope](#c-global-scope)
        - [Example: Global Scope](#example-global-scope)
        - [Example: Modifying Global Variables](#example-modifying-global-variables)
    - [Built-in Scope](#d-built-in-scope)
        - [Example: Built-in Scope](#example-built-in-scope)
3. [Advanced Concepts](#3-advanced-concepts)
    - [Scope Resolution Order (LEGB Rule)](#a-scope-resolution-order-legb-rule)
        - [Example: LEGB Rule](#example-legb-rule)
    - [Shadowing](#b-shadowing)
        - [Example: Shadowing](#example-shadowing)
    - [Nested Functions and Closures](#c-nested-functions-and-closures)
        - [Example: Closure](#example-closure)
4. [Best Practices](#4-best-practices)
5. [Practical Use Cases](#5-practical-use-cases)
    - [Function Arguments and Local Scope](#a-function-arguments-and-local-scope)
        - [Example: Function Arguments and Local Scope](#example-function-arguments-and-local-scope)
    - [Managing State with Enclosing Scope](#b-managing-state-with-enclosing-scope)
        - [Example: Managing State with Enclosing Scope](#example-managing-state-with-enclosing-scope)
    - [Using Global Constants](#c-using-global-constants)
        - [Example: Using Global Constants](#example-using-global-constants)
    - [Debugging Scope Issues](#d-debugging-scope-issues)
        - [Example: Debugging Scope Issues](#example-debugging-scope-issues)
6. [Common Pitfalls](#6-common-pitfalls)
    - [Unintended Shadowing](#a-unintended-shadowing)
        - [Example: Unintended Shadowing](#example-unintended-shadowing)
    - [Modifying Mutable Globals](#b-modifying-mutable-globals)
        - [Example: Modifying Mutable Globals](#example-modifying-mutable-globals)

# Scopes in Python

- define the visibility and accessibility of variables, functions, and objects within a program.

## 1. Basic Understanding of Scopes

### What is Scope?

refers to the region of a program where a variable or name is accessible. Python has several types of scopes, each with its own rules for accessing and modifying variables.

### Types of Scopes

Python follows the **LEGB Rule** to determine the order in which scopes are searched when resolving a variable:

- **L (Local):** Variables defined inside the current function.
- **E (Enclosing):** Variables in the enclosing (outer) function, if any.
- **G (Global):** Variables defined at the top level of a module or explicitly declared as `global`.
- **B (Built-in):** Predefined names provided by Python (e.g., `print`, `len`).

The interpreter searches for a variable in this order: **Local → Enclosing → Global → Built-in**.

## 2. Types of Scopes in Detail

### a. Local Scope

Variables defined inside a function are local to that function and cannot be accessed outside it.

#### Example: Local Scope

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()
# print(x)  # Raises NameError: name 'x' is not defined
```

### b. Enclosing (Nonlocal) Scope

When a function is nested inside another function, the inner function can access variables from the outer function's scope. These variables are part of the enclosing scope.

#### Example: Enclosing Scope

```python
def outer_function():
    y = 20  # Enclosing variable

    def inner_function():
        print(y)  # Accessing enclosing variable

    inner_function()

outer_function()
```

To modify an enclosing variable, you must use the `nonlocal` keyword.

#### Example: Modifying Enclosing Variables

```python
def outer_function():
    y = 20

    def inner_function():
        nonlocal y
        y += 5
        print(y)

    inner_function()

outer_function()  # Output: 25
```

### c. Global Scope

Variables defined at the top level of a module or script are global. They can be accessed anywhere in the module unless shadowed by a local variable.

#### Example: Global Scope

```python
z = 30  # Global variable

def my_function():
    print(z)

my_function()  # Output: 30
```

To modify a global variable inside a function, you must declare it as `global`.

#### Example: Modifying Global Variables

```python
z = 30

def my_function():
    global z
    z += 10
    print(z)

my_function()  # Output: 40
print(z)       # Output: 40
```

### d. Built-in Scope

Python provides a set of predefined names in the built-in scope, such as `print`, `len`, `range`, etc. These names are always available unless overridden.

#### Example: Built-in Scope

```python
print(len("Hello"))  # Output: 5

# Shadowing a built-in name
len = "custom value"
# print(len("Hello"))  # Raises TypeError: 'str' object is not callable
```

## 3. Advanced Concepts

### a. Scope Resolution Order (LEGB Rule)

Python resolves variable names in the following order:

1. **Local:** Check the current function's scope.
2. **Enclosing:** Check the enclosing function's scope (if nested).
3. **Global:** Check the module-level scope.
4. **Built-in:** Check the built-in scope.

#### Example: LEGB Rule

```python
x = "global"  # Global variable

def outer_function():
    x = "enclosing"  # Enclosing variable

    def inner_function():
        x = "local"  # Local variable
        print(x)  # Output: local

    inner_function()
    print(x)  # Output: enclosing

outer_function()
print(x)  # Output: global
```

### b. Shadowing

Shadowing occurs when a variable in a narrower scope has the same name as a variable in a broader scope. The narrower scope "shadows" the broader scope, making the broader variable inaccessible within the narrower scope.

#### Example: Shadowing

```python
x = "global"

def my_function():
    x = "local"
    print(x)  # Output: local

my_function()
print(x)  # Output: global
```

### c. Nested Functions and Closures

A closure is a function object that remembers values in its enclosing scope, even if the outer function has finished executing.

#### Example: Closure

```python
def outer_function():
    message = "Hello"

    def inner_function():
        print(message)  # Accessing enclosing variable

    return inner_function

closure = outer_function()
closure()  # Output: Hello
```

## **4. Best Practices**

1. **Minimize Global Variables:** Avoid using global variables whenever possible. They can lead to unpredictable behavior and make debugging harder.
2. **Use `global` and `nonlocal` Sparingly:** Modify global or enclosing variables only when absolutely necessary.
3. **Avoid Shadowing Built-ins:** Do not reuse names like `list`, `dict`, or `print` as variable names.
4. **Keep Scopes Small:** Limit the scope of variables to the smallest region where they are needed.
5. **Document Scope Usage:** Clearly document where variables are defined and how they are used.

## 5. Practical Use Cases

### a. Function Arguments and Local Scope

Function arguments create a local scope for the function.

```python
def greet(name):
    greeting = f"Hello, {name}!"
    print(greeting)

greet("Alice")  # Output: Hello, Alice!
# print(greeting)  # Raises NameError: name 'greeting' is not defined
```

### b. Managing State with Enclosing Scope

Enclosing scope is useful for managing state in nested functions.

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter_instance = counter()
print(counter_instance())  # Output: 1
print(counter_instance())  # Output: 2
```

### c. Using Global Constants

Global variables can be used for constants that do not change during execution.

```python
PI = 3.14159

def calculate_area(radius):
    return PI * radius ** 2

print(calculate_area(5))  # Output: 78.53975
```

### d. Debugging Scope Issues

Understanding scope helps debug issues like unintended variable overwrites.

```python
x = 10

def my_function():
    x = 20  # Shadows the global x
    print(x)  # Output: 20

my_function()
print(x)  # Output: 10
```

## 6. Common Pitfalls

### a. Unintended Shadowing

Accidentally reusing a variable name can lead to unexpected behavior.

```python
def my_function():
    list = [1, 2, 3]  # Shadows the built-in list type
    print(list)  # Output: [1, 2, 3]

my_function()
# print(list("abc"))  # Raises TypeError: 'list' object is not callable
```

### b. Modifying Mutable Globals

Modifying mutable global variables (e.g., lists or dictionaries) can have side effects.

```python
data = []

def add_item(item):
    data.append(item)

add_item(1)
print(data)  # Output: [1]
```
