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

# Generators

- create iterators in a concise and memory-efficient way.
  - especially useful for handling large datasets, streaming data, or any scenario where you want to generate values on-the-fly without storing them all in memory at once.

## 1. Basic Understanding of Generators

### What is a Generator?

A generator is a special type of iterator that generates values one at a time using the `yield` keyword. Unlike regular functions that return a value and terminate, generators "pause" their execution when they encounter `yield`, and resume from where they left off when the next value is requested.

### Syntax

Generators can be created using:

1. **Generator Functions:** Functions that use `yield`.
2. **Generator Expressions:** Similar to list comprehensions but use parentheses instead of square brackets.

#### Example: A Simple Generator Function

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(next(gen))  # Raises StopIteration
```

> **Note:** Calling `next()` on a generator advances its execution to the next `yield` statement.
> - Once all values are exhausted, a `StopIteration` exception is raised.

#### Example: A Generator Expression

```python
gen_expr = (x**2 for x in range(5))
print(next(gen_expr))  # Output: 0
print(next(gen_expr))  # Output: 1
print(next(gen_expr))  # Output: 4
```

## 2. Advanced Concepts

### Lazy Evaluation

Generators evaluate values lazily, meaning they produce values only when requested. This makes them highly memory-efficient for large datasets or infinite sequences.

#### Example: Infinite Sequence

```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
for _ in range(5):
    print(next(gen))  # Output: 0, 1, 2, 3, 4
```

### Chaining Generators

You can chain multiple generators together using `yield from`. This allows you to delegate part of the generation process to another generator.

#### Example: Chaining Generators

```python
def sub_generator():
    yield "Hello"
    yield "World"

def main_generator():
    yield from sub_generator()
    yield "!"

gen = main_generator()
print(" ".join(gen))  # Output: Hello World !
```

### Sending Data to Generators

Generators can also receive data using the `.send()` method. This allows two-way communication between the generator and the caller.

#### Example: Sending Data

```python
def echo_generator():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")  # Output: Received: Hello
gen.send("World")  # Output: Received: World
```

### Throwing Exceptions

You can throw exceptions into a generator using the `.throw()` method.

#### Example: Throwing Exceptions

```python
def sensitive_generator():
    try:
        yield "Normal operation"
        yield "Still working"
    except ValueError:
        yield "Caught an exception!"

gen = sensitive_generator()
print(next(gen))  # Output: Normal operation
print(gen.throw(ValueError))  # Output: Caught an exception!
```

## 3. Custom Generators

Custom generators are generators tailored to specific needs. Below are some examples:

### a. File Line Reader

A generator to read a file line by line without loading the entire file into memory:

```python
def file_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

for line in file_reader('example.txt'):
    print(line)
```

### b. Fibonacci Sequence

A generator to produce an infinite Fibonacci sequence:

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34
```

### c. Batch Processing

A generator to process data in batches:

```python
def batch_process(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

data = list(range(10))
for batch in batch_process(data, 3):
    print(batch)  # Output: [0, 1, 2], [3, 4, 5], [6, 7, 8], [9]
```

## 4. Best Practices

1. **Use Generators for Large Datasets:** Generators are ideal for handling large datasets or streams because they avoid loading everything into memory.
2. **Avoid Side Effects:** Keep generators pure—avoid modifying global state or introducing side effects.
3. **Document Behavior:** Clearly document what the generator produces, its inputs, and any assumptions it makes.
4. **Test Edge Cases:** Test generators with edge cases like empty inputs, infinite loops, or unexpected types.
5. **Combine with Other Tools:** Use generators with tools like `itertools` for advanced iteration patterns.

## 5. Practical Use Cases

### a. Streaming Data

Generators are perfect for streaming data from APIs, databases, or files. For example:

```python
import requests

def stream_data(url):
    response = requests.get(url, stream=True)
    for chunk in response.iter_content(chunk_size=1024):
        yield chunk

for chunk in stream_data("https://example.com/large-file"):
    process(chunk)
```

### b. Pipelines

Generators can be used to build data processing pipelines:

```python
def producer():
    for i in range(10):
        yield i

def processor(source):
    for item in source:
        yield item * 2

def consumer(source):
    for item in source:
        print(item)

pipeline = consumer(processor(producer()))
```

### c. Coroutine-Based Systems

Generators can be used to implement coroutines for cooperative multitasking:

```python
def task(name, interval):
    while True:
        print(f"{name} is running")
        yield

def scheduler(tasks):
    while True:
        for task in tasks:
            next(task)

tasks = [task("Task 1", 1), task("Task 2", 2)]
scheduler(tasks)
```

## 6. Combining Generators with `itertools`

The `itertools` module provides powerful tools for working with iterators and generators.

#### Example: Infinite Count

```python
from itertools import count

def even_numbers():
    for num in count(start=0, step=2):
        yield num

evens = even_numbers()
for _ in range(5):
    print(next(evens))  # Output: 0, 2, 4, 6, 8
```

#### Example: Grouping Data

```python
from itertools import groupby

data = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
grouped = groupby(data, key=lambda x: x[0])

for key, group in grouped:
    print(key, list(group))
# Output:
# a [('a', 1), ('a', 2)]
# b [('b', 3), ('b', 4)]
```

By mastering generators, you can write efficient, scalable, and elegant code. They are particularly valuable in scenarios involving large datasets, streaming, or asynchronous workflows.
