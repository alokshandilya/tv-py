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
>
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

# Iterators

- fundamental concept in Python that
  - allow you to traverse through elements of a collection (like lists, tuples, dictionaries, etc.) one at a time.
- closely related to generators but differ in their implementation and use cases.

## 1. Basic Understanding of Iterators

### What is an Iterator?

An iterator is an object that implements two methods:

1. `__iter__()`: Returns the iterator object itself.
2. `__next__()`: Returns the next value in the sequence. If there are no more items, it raises a `StopIteration` exception.

Iterators are used internally by Python constructs like `for` loops to iterate over collections.

### How Iterators Work

When you use a `for` loop, Python internally calls the `__iter__()` method on the iterable (e.g., a list) to get an iterator, and then repeatedly calls `__next__()` on the iterator until `StopIteration` is raised.

#### Example: Using an Iterator

```python
my_list = [1, 2, 3]
iterator = iter(my_list)  # Calls __iter__()
print(next(iterator))  # Calls __next__() -> Output: 1
print(next(iterator))  # Calls __next__() -> Output: 2
print(next(iterator))  # Calls __next__() -> Output: 3
# print(next(iterator))  # Raises StopIteration
```

## 2. Custom Iterators

You can create your own iterators by defining a class that implements the `__iter__()` and `__next__()` methods.

### a. Simple Custom Iterator

Here’s an example of a custom iterator that generates numbers up to a given limit:

```python
class CountUpTo:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self  # The iterator object is itself

    def __next__(self):
        if self.current < self.max_value:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = CountUpTo(5)
for num in counter:
    print(num)  # Output: 1, 2, 3, 4, 5
```

### b. Infinite Iterator

You can also create an infinite iterator by never raising `StopIteration`:

```python
class InfiniteCounter:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current

infinite_counter = InfiniteCounter()
for num in infinite_counter:
    print(num)  # Prints numbers indefinitely
    if num > 5:  # Break manually to avoid infinite loop
        break
```

### c. Iterator with State

Custom iterators can maintain state between iterations. For example, here’s an iterator that alternates between two values:

```python
class Alternator:
    def __init__(self, value1, value2):
        self.values = [value1, value2]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.values[self.index]
        self.index = (self.index + 1) % 2  # Alternate between 0 and 1
        return value

alternator = Alternator("A", "B")
for _ in range(6):
    print(next(alternator))  # Output: A, B, A, B, A, B
```

## 3. Advanced Concepts

### a. Combining Iterators

You can combine multiple iterators using tools like `itertools.chain`.

#### Example: Combining Iterators

```python
from itertools import chain

class RangeIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            self.start += 1
            return self.start - 1
        else:
            raise StopIteration

iterator1 = RangeIterator(1, 3)
iterator2 = RangeIterator(4, 6)

combined = chain(iterator1, iterator2)
for num in combined:
    print(num)  # Output: 1, 2, 3, 4, 5
```

### b. Lazy Evaluation

Custom iterators can implement lazy evaluation, meaning they compute values only when requested. This is useful for handling large datasets or infinite sequences.

#### Example: Lazy Fibonacci Iterator

```python
class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

fib = FibonacciIterator()
for _ in range(10):
    print(next(fib), end=" ")  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

## 4. Best Practices

1. **Separate Iterables and Iterators:** Keep the iterable (the object that produces iterators) separate from the iterator itself. For example, a list is an iterable, while its iterator is created by calling `iter()`.
2. **Handle Edge Cases:** Ensure your iterator handles edge cases like empty data or invalid inputs gracefully.
3. **Avoid Side Effects:** Keep iterators pure—avoid modifying global state or introducing side effects.
4. **Document Behavior:** Clearly document what the iterator produces, its inputs, and any assumptions it makes.
5. **Use Built-in Tools:** Leverage Python’s built-in tools like `itertools` for common iterator patterns instead of reinventing the wheel.

## 5. Practical Use Cases

### a. File Line Reader

A custom iterator to read a file line by line without loading the entire file into memory:

```python
class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        self.file = open(self.file_path, 'r')
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()

for line in FileReader('example.txt'):
    print(line)
```

### b. Pagination

A custom iterator to handle paginated API responses:

```python
class Paginator:
    def __init__(self, api_client, endpoint, page_size):
        self.api_client = api_client
        self.endpoint = endpoint
        self.page_size = page_size
        self.current_page = 0
        self.total_pages = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.total_pages is None or self.current_page < self.total_pages:
            response = self.api_client.get(self.endpoint, params={"page": self.current_page, "size": self.page_size})
            self.total_pages = response['total_pages']
            self.current_page += 1
            return response['data']
        else:
            raise StopIteration

# Usage
paginator = Paginator(api_client, "/items", 10)
for page in paginator:
    process(page)
```

### c. Custom Data Structures

You can create custom data structures that support iteration. For example, a binary tree iterator:

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTreeIterator:
    def __init__(self, root):
        self.stack = []
        self.push_left(root)

    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        if node.right:
            self.push_left(node.right)
        return node.value

# Example Tree
root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
tree_iterator = BinaryTreeIterator(root)
for value in tree_iterator:
    print(value)  # Output: 1, 2, 3, 4, 5, 6, 7
```

## 6. Iterators vs Generators

| Feature           | Iterator                        | Generator                            |
| ----------------- | ------------------------------- | ------------------------------------ |
| Implementation    | Requires defining a class       | Defined using functions with `yield` |
| Memory Efficiency | Can be memory-efficient         | Always memory-efficient              |
| Complexity        | More verbose                    | Concise and easier to write          |
| State Management  | Explicitly managed in the class | Managed automatically by Python      |
| Reusability       | Can be reused                   | Cannot be reused once exhausted      |

Generators are often preferred for simplicity and readability, while iterators are useful when you need more control or are implementing complex behavior.

Iterators are particularly valuable for creating custom data structures, handling large datasets, or implementing specialized traversal logic.
