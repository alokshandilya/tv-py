# Decorators

- Decorators allow to modify or extend the behavior of functions, methods, or classes without changing their actual code.
- are widely used for cross-cutting concerns like logging, access control, memoization, timing, and more.

## 1. Basic Understanding of Decorators

### What is a Decorator?

A decorator is a function that takes another function (or class) as input and returns a new function (or class) with added or modified behavior. It essentially "wraps" the original function or class.

### Syntax

The `@decorator_name` syntax is syntactic sugar for applying a decorator to a function or class:

```python
@decorator
def my_function():
    pass
```

This is equivalent to:

```python
def my_function():
    pass
my_function = decorator(my_function)
```

### Basic Example

Here’s a simple decorator that prints a message before and after a function is called:

```python
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**

```
Before the function call
Hello!
After the function call
```

## 2. Advanced Concepts

### Decorators with Arguments

Sometimes, you want to pass arguments to a decorator. To achieve this, you need to create a decorator factory—a function that returns a decorator.

#### Example: Logging with Custom Messages

```python
def log_with_message(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{message}: Entering {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{message}: Exiting {func.__name__}")
            return result
        return wrapper
    return decorator

@log_with_message("DEBUG")
def add(a, b):
    return a + b

print(add(3, 5))
```

**Output:**

```
DEBUG: Entering add
DEBUG: Exiting add
8
```

### Preserving Metadata

When you wrap a function with a decorator, the metadata (like `__name__`, `__doc__`, etc.) of the original function is lost. To preserve it, use the `functools.wraps` decorator.

#### Example: Using `functools.wraps`

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Greet someone."""
    print(f"Hello, {name}!")

print(greet.__name__)  # Output: greet
print(greet.__doc__)   # Output: Greet someone.
```

## 3. Custom Decorators

Custom decorators are decorators tailored to specific needs. Below are some common use cases:

### a. Timing Functions

A decorator to measure the execution time of a function:

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()
```

**Output:**

```
slow_function executed in 2.0002 seconds
```

### b. Access Control

A decorator to restrict access based on user roles:

```python
def requires_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = kwargs.get('user_role', 'guest')
            if user_role != role:
                raise PermissionError(f"User does not have the required role: {role}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@requires_role('admin')
def delete_user(user_role='guest'):
    print("User deleted.")

try:
    delete_user(user_role='guest')  # Raises PermissionError
except PermissionError as e:
    print(e)
```

**Output:**

```
User does not have the required role: admin
```

### c. Caching (Memoization)

A decorator to cache the results of expensive function calls:

```python
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print("Fetching from cache")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Computes and caches values
print(fibonacci(10))  # Fetches from cache
```

## 4. Class-Based Decorators

You can also create decorators using classes by implementing the `__call__` method.

#### Example: A Simple Class-Based Decorator

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"Call {self.call_count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")

say_hi()
say_hi()
```

**Output:**

```
Call 1 to say_hi
Hi!
Call 2 to say_hi
Hi!
```

## 5. Best Practices

1. **Use `functools.wraps`:** Always use `functools.wraps` to preserve the metadata of the original function.
2. **Keep Decorators Simple:** Avoid overly complex logic inside decorators. If the logic becomes too complicated, consider breaking it into smaller helper functions.
3. **Document Your Decorators:** Clearly document what the decorator does, its parameters, and its behavior.
4. **Test Decorators Thoroughly:** Since decorators modify the behavior of functions, ensure they are tested in various scenarios.
5. **Avoid Side Effects:** Decorators should ideally be pure functions—avoid modifying global state or introducing unexpected side effects.

## 6. Practical Use Cases

- **Logging:** Add logging to functions for debugging purposes.
- **Authentication and Authorization:** Restrict access to certain functions or APIs based on user roles.
- **Performance Monitoring:** Measure the execution time of functions.
- **Caching:** Cache results of expensive computations to improve performance.
- **Validation:** Validate inputs to functions or methods.

By mastering decorators, you can write cleaner, reusable, and modular code.
