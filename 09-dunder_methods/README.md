> Dunder methods (short for "double underscore methods") are special methods in Python that allow you to define custom behavior for built-in operations and interactions with objects. These methods are surrounded by double underscores (`__`), such as `__init__`, `__str__`, and `__add__`. They enable you to customize how your classes interact with Python's built-in functions, operators, and protocols.

## 1. What Are Dunder Methods?

### Purpose

Dunder methods allow you to override or extend the default behavior of Python's built-in operations. For example:

- How an object is initialized (`__init__`).
- How an object is represented as a string (`__str__` or `__repr__`).
- How operators like `+`, `-`, or `==` behave with your objects (`__add__`, `__sub__`, `__eq__`).

These methods make your classes more Pythonic by integrating seamlessly with Python's syntax and features.

### Syntax

Dunder methods are defined inside a class and follow the naming convention `__method_name__`.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value: {self.value}"

obj = MyClass(42)
print(obj)  # Output: MyClass with value: 42
```

## 2. Common Dunder Methods

Here’s a list of commonly used dunder methods, grouped by functionality:

### a. Object Initialization and Representation

These methods control how objects are created and displayed.

| Method                | Description                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------ |
| `__init__(self, ...)` | Initializes a new instance of the class.                                                   |
| `__new__(cls, ...)`   | Creates a new instance of the class (rarely overridden).                                   |
| `__repr__(self)`      | Returns an "official" string representation of the object (used by `repr`).                |
| `__str__(self)`       | Returns a "user-friendly" string representation of the object (used by `str` and `print`). |

#### Example

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))  # Output: Point(3, 4)
print(str(p))   # Output: (3, 4)
print(p)        # Output: (3, 4)
```

### b. Comparison Operators

These methods define how comparison operators (`==`, `!=`, `<`, etc.) work with your objects.

| Method                | Operator/Function |
| --------------------- | ----------------- |
| `__eq__(self, other)` | `==`              |
| `__ne__(self, other)` | `!=`              |
| `__lt__(self, other)` | `<`               |
| `__le__(self, other)` | `<=`              |
| `__gt__(self, other)` | `>`               |
| `__ge__(self, other)` | `>=`              |

#### Example

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

n1 = Number(5)
n2 = Number(10)
print(n1 == n2)  # Output: False
print(n1 < n2)   # Output: True
```

### c. Arithmetic Operators

These methods define how arithmetic operators (`+`, `-`, `*`, etc.) work with your objects.

| Method                      | Operator/Function |
| --------------------------- | ----------------- |
| `__add__(self, other)`      | `+`               |
| `__sub__(self, other)`      | `-`               |
| `__mul__(self, other)`      | `*`               |
| `__truediv__(self, other)`  | `/`               |
| `__floordiv__(self, other)` | `//`              |
| `__mod__(self, other)`      | `%`               |
| `__pow__(self, other)`      | `**`              |

#### Example

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: Vector(4, 6)
```

### d. Container and Iterator Protocols

These methods allow your objects to behave like containers or iterators.

| Method                          | Description                                               |
| ------------------------------- | --------------------------------------------------------- |
| `__len__(self)`                 | Returns the length of the object (used by `len()`).       |
| `__getitem__(self, key)`        | Accesses elements using indexing (`obj[key]`).            |
| `__setitem__(self, key, value)` | Sets elements using indexing (`obj[key] = value`).        |
| `__delitem__(self, key)`        | Deletes elements using indexing (`del obj[key]`).         |
| `__iter__(self)`                | Returns an iterator for the object (used by `for` loops). |
| `__next__(self)`                | Defines the next item in an iterator (used by `next()`).  |

#### Example

```python
class MyList:
    def __init__(self, *args):
        self.data = list(args)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

lst = MyList(1, 2, 3)
print(len(lst))      # Output: 3
print(lst[1])        # Output: 2
lst[1] = 42
print(lst[1])        # Output: 42
```

### e. Callable Objects

The `__call__` method allows instances of a class to be called like functions.

| Method                | Description                                                |
| --------------------- | ---------------------------------------------------------- |
| `__call__(self, ...)` | Allows an instance to be called like a function (`obj()`). |

#### Example

```python
class Adder:
    def __init__(self, base):
        self.base = base

    def __call__(self, x):
        return self.base + x

add_five = Adder(5)
print(add_five(10))  # Output: 15
```

### f. Context Management

These methods enable your objects to work with the `with` statement.

| Method                                           | Description                          |
| ------------------------------------------------ | ------------------------------------ |
| `__enter__(self)`                                | Called when entering a `with` block. |
| `__exit__(self, exc_type, exc_value, traceback)` | Called when exiting a `with` block.  |

#### Example

```python
class ResourceManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with ResourceManager() as resource:
    print("Inside context")
# Output:
# Entering context
# Inside context
# Exiting context
```

### g. Attribute Access

These methods control how attributes are accessed, set, or deleted.

| Method                           | Description                                     |
| -------------------------------- | ----------------------------------------------- |
| `__getattr__(self, name)`        | Called when accessing a non-existent attribute. |
| `__setattr__(self, name, value)` | Called when setting an attribute.               |
| `__delattr__(self, name)`        | Called when deleting an attribute.              |

#### Example

```python
class DynamicAttributes:
    def __getattr__(self, name):
        return f"Attribute '{name}' not found"

    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

obj = DynamicAttributes()
print(obj.some_attr)  # Output: Attribute 'some_attr' not found
obj.new_attr = 42     # Output: Setting new_attr to 42
```

## 3. Available Dunder Methods

Here’s a comprehensive list of commonly available dunder methods:

### Object Lifecycle

- `__new__`
- `__init__`
- `__del__`

### String Representations

- `__repr__`
- `__str__`
- `__format__`
- `__bytes__`

### Comparison Operators

- `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`

### Arithmetic Operators

- `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`, etc.

### Container Protocols

- `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__next__`, `__contains__`

### Callable Objects

- `__call__`

### Context Management

- `__enter__`, `__exit__`

### Attribute Access

- `__getattr__`, `__setattr__`, `__delattr__`, `__dir__`

### Hashing and Equality

- `__hash__`, `__bool__`

### Descriptors

- `__get__`, `__set__`, `__delete__`

## 4. Practical Use Cases

### a. Custom Data Structures

Define custom lists, dictionaries, or sets with specialized behavior.

```python
class LimitedList:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = []

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def append(self, value):
        if len(self.data) < self.max_size:
            self.data.append(value)
        else:
            raise OverflowError("List is full")

lst = LimitedList(3)
lst.append(1)
lst.append(2)
print(len(lst))  # Output: 2
```

### b. Operator Overloading

Create classes that support mathematical operations.

```python
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)
c3 = c1 + c2
print(c3)  # Output: 4 + 6i
```

### c. Context Managers

Manage resources like files or locks.

```python
class FileHandler:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileHandler('example.txt', 'w') as file:
    file.write("Hello, World!")
```

By mastering dunder methods, you can create highly customizable and Pythonic classes that integrate seamlessly with Python's built-in features. Use them judiciously to enhance your code without overcomplicating it.

Let’s implement each of the specified dunder methods (`__call__`, `__new__`, `__str__`, `__repr__`, `__dict__`, `__len__`, `__next__`, `__enter__`, `__exit__`) in Python with practical examples. Each method will be explained step by step.

### 1. `__call__`

The `__call__` method allows an instance of a class to be called like a function.

#### Implementation

```python
class CallableExample:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, x):
        return self.multiplier * x

# Usage
callable_obj = CallableExample(5)
print(callable_obj(10))  # Output: 50
```

### 2. `__new__`

The `__new__` method is responsible for creating a new instance of a class. It is rarely overridden but can be useful for customizing object creation (e.g., singleton patterns).

#### Implementation

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

# Usage
obj1 = Singleton(10)
obj2 = Singleton(20)
print(obj1.value)  # Output: 20 (Singleton behavior)
print(obj2.value)  # Output: 20
print(obj1 is obj2)  # Output: True
```

### 3. `__str__`

The `__str__` method defines the "user-friendly" string representation of an object, used by `print()` and `str()`.

#### Implementation

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

# Usage
person = Person("Alice", 30)
print(person)  # Output: Alice is 30 years old.
```

### 4. `__repr__`

The `__repr__` method defines the "official" string representation of an object, used by `repr()` and debugging tools. It should ideally be unambiguous and recreate the object if possible.

#### Implementation

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Usage
p = Point(3, 4)
print(repr(p))  # Output: Point(3, 4)
```

### 5. `__dict__`

The `__dict__` attribute is a dictionary that stores an object's attributes. You cannot directly override `__dict__`, but you can manipulate it or use `__slots__` to disable it.

#### Implementation

```python
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Usage
obj = MyClass(10, 20)
print(obj.__dict__)  # Output: {'x': 10, 'y': 20}
```

If you use `__slots__`, the `__dict__` attribute is disabled:

```python
class MyClassWithSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Usage
obj = MyClassWithSlots(10, 20)
# print(obj.__dict__)  # AttributeError: 'MyClassWithSlots' object has no attribute '__dict__'
```

### 6. `__len__`

The `__len__` method defines the behavior of the `len()` function when applied to an object.

#### Implementation

```python
class MyList:
    def __init__(self, *args):
        self.data = list(args)

    def __len__(self):
        return len(self.data)

# Usage
lst = MyList(1, 2, 3)
print(len(lst))  # Output: 3
```

---

### 7. `__next__`

The `__next__` method defines the behavior of the `next()` function for iterators. It must raise `StopIteration` when there are no more items.

#### Implementation

```python
class Counter:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_value:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Usage
counter = Counter(3)
for num in counter:
    print(num)  # Output: 1, 2, 3
```

### 8. `__enter__` and `__exit__`

The `__enter__` and `__exit__` methods enable an object to work with the `with` statement, typically for resource management.

#### Implementation

```python
class FileHandler:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        print("File opened")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed")

# Usage
with FileHandler('example.txt', 'w') as file:
    file.write("Hello, World!")
# Output:
# File opened
# File closed
```

## Complete Example Combining All Methods

Here’s a single class that demonstrates all the implemented methods:

```python
class MultiFunctional:
    __slots__ = ('name', 'age', '_data')

    def __new__(cls, *args, **kwargs):
        print("Creating a new instance...")
        return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._data = [1, 2, 3]

    def __call__(self, multiplier):
        return [x * multiplier for x in self._data]

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"MultiFunctional(name={self.name}, age={self.age})"

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self._data):
            result = self._data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

# Usage
obj = MultiFunctional("Alice", 30)
print(obj)  # Output: Alice is 30 years old.
print(repr(obj))  # Output: MultiFunctional(name=Alice, age=30)
print(len(obj))  # Output: 3
print(obj(2))  # Output: [2, 4, 6]

for item in obj:
    print(item)  # Output: 1, 2, 3

with obj:
    print("Inside context")
# Output:
# Entering context
# Inside context
# Exiting context
```

## Key Takeaways

- Use `__call__` to make objects callable like functions.
- Override `__new__` for custom object creation logic (e.g., singletons).
- Implement `__str__` for user-friendly representations and `__repr__` for debugging.
- Use `__len__` to define the length of an object.
- Implement `__next__` and `__iter__` to make objects iterable.
- Use `__enter__` and `__exit__` for context management with the `with` statement.

By mastering these dunder methods, you can create highly customizable and Pythonic classes that integrate seamlessly with Python's built-in features.

## diff b/w `__new__` and `__init__`

In Python, both `__new__` and `__init__` are special methods that play crucial roles in object creation and initialization. However, they serve distinct purposes:

### `__new__(cls, *args, **kwargs)`

- **Purpose:** Responsible for creating and returning a new instance of a class. It's the first step in object instantiation.
- **When it's called:** Before `__init__`.
- **What it does:**
  - Takes the class (`cls`) as its first argument.
  - Can be used to customize object creation (e.g., implementing singletons, controlling object type).
  - Must return the newly created object (usually by calling `super().__new__(cls, *args, **kwargs)`).
- **Use cases:**
  - Creating immutable objects (e.g., strings, tuples).
  - Implementing design patterns like Singleton (ensuring only one instance of a class is created).
  - Customizing object creation logic.

### `__init__(self, *args, **kwargs)`

- **Purpose:** Initializes the newly created object's attributes.
- **When it's called:** After `__new__`.
- **What it does:**
  - Takes the instance (`self`) as its first argument.
  - Sets up the object's attributes based on the provided arguments.
  - Does not return any value (it implicitly returns `None`).
- **Use cases:**
  - Setting initial values for instance variables.
  - Performing any setup required for the object to function correctly.

**Key Differences**

| Feature              | `__new__`                          | `__init__`                             |
| -------------------- | ---------------------------------- | -------------------------------------- |
| **Purpose**          | Object creation                    | Object initialization                  |
| **When it's called** | Before `__init__`                  | After `__new__`                        |
| **Arguments**        | `cls` (class), `*args`, `**kwargs` | `self` (instance), `*args`, `**kwargs` |
| **Return value**     | The new object instance            | `None`                                 |

**Example**

```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating a new MyClass object")
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, name, age):
        print("Initializing the MyClass object")
        self.name = name
        self.age = age

obj = MyClass("Alice", 30)
```

**Output:**

```
Creating a new MyClass object
Initializing the MyClass object
```

**In summary:**

- `__new__` is like the factory that builds the object.
- `__init__` is like the decorator who furnishes the object with its attributes.

In most common scenarios, you'll primarily use `__init__` to initialize your objects. `__new__` is typically used in more advanced cases where you need to control the object creation process itself.

## `__repr__` vs `__str__`

In Python, both `__repr__` and `__str__` are special methods (also known as "dunder" methods) that define how objects of a class are represented as strings. However, they serve different purposes and are used in different contexts.

### 1. **`__repr__` Method**

- **Purpose**: The `__repr__` method is intended to provide an "official" string representation of an object, which should ideally be unambiguous and can be used to recreate the object if possible.
- **Usage**: It is primarily used for debugging and development purposes. When you type an object in the Python interpreter or use functions like `repr()`, Python calls the `__repr__` method.
- **Goal**: The goal of `__repr__` is to be as explicit and informative as possible, often including details about the object's state or structure.

#### Example:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(10, 20)
print(repr(p))  # Output: Point(10, 20)
```

In this example, `__repr__` provides a clear and unambiguous representation of the `Point` object, which could even be used to recreate the object by copying and pasting the output.

### 2. `__str__` Method

- **Purpose**: The `__str__` method is intended to provide a "user-friendly" or "informal" string representation of an object, which is meant to be readable by end-users.
- **Usage**: It is called by the `print()` function, `str()`, or when you try to convert an object to a string using `str(obj)`.
- **Goal**: The goal of `__str__` is to make the output more human-readable and concise, without necessarily including all the details of the object.

#### Example:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(10, 20)
print(str(p))  # Output: (10, 20)
print(p)       # Output: (10, 20)
```

In this example, `__str__` provides a simpler, more user-friendly representation of the `Point` object, which is easier to read but less detailed than the `__repr__` output.

### Key Differences:

| Feature              | `__repr__`                                                                                                                   | `__str__`                                                     |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Purpose**          | Unambiguous, detailed representation                                                                                         | Readable, user-friendly representation                        |
| **Called by**        | `repr(obj)`, `print()` in interactive mode                                                                                   | `str(obj)`, `print(obj)`                                      |
| **Default behavior** | If `__repr__` is not defined, Python uses a default implementation that includes the object's class name and memory address. | If `__str__` is not defined, Python falls back to `__repr__`. |
| **Use case**         | Debugging, logging, development                                                                                              | Displaying information to end-users                           |

### Default Behavior:

- If you don't define either `__repr__` or `__str__` in your class, Python will use the default implementation of `__repr__`, which looks something like `<__main__.Point object at 0x7f8b1c2d3e50>`.
- If you define `__repr__` but not `__str__`, Python will use `__repr__` as a fallback for `__str__`.

#### Example of Default Behavior:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)

print(repr(p))  # Output: <__main__.Point object at 0x7f8b1c2d3e50>
print(str(p))   # Output: <__main__.Point object at 0x7f8b1c2d3e50>
```

Here, since neither `__repr__` nor `__str__` is defined, Python uses the default `__repr__` for both `repr(p)` and `str(p)`.

### Best Practices:

1. **Always Define `__repr__`**: It's a good practice to always define `__repr__` because it provides a clear and unambiguous representation of the object, which is useful for debugging.
2. **Optionally Define `__str__`**: You can define `__str__` if you want a more user-friendly representation for end-users, but it's optional. If you don't define `__str__`, Python will fall back to `__repr__`.

3. **Make `__repr__` Recreatable**: Ideally, the output of `__repr__` should be valid Python code that can recreate the object. For example, `Point(10, 20)` is a valid Python expression that can recreate the `Point` object.

### Summary:

- **`__repr__`**: Provides an unambiguous, detailed representation of an object, mainly for debugging and development.
- **`__str__`**: Provides a user-friendly, readable representation of an object, mainly for end-user display.

Both methods are important for controlling how your objects are displayed in different contexts, and defining them appropriately can improve the usability and clarity of your classes.

> Certainly! The idea behind making the `__repr__` method "recreatable" is that the string returned by `__repr__` should ideally be valid Python code that, when executed, would recreate the original object. This is particularly useful for debugging and development because it allows developers to easily understand and reproduce the state of an object.

### Why Make `__repr__` Recreatable?

1. **Debugging**: When you're debugging, having a representation of an object that can be directly used to recreate it is extremely helpful. You can copy-paste the output into your code or interpreter to recreate the exact state of the object.
2. **Reproducibility**: If you log the state of objects during execution (e.g., in logs or error messages), having a recreatable representation ensures that you can later reproduce the exact conditions that led to a bug or issue.

3. **Clarity**: A recreatable `__repr__` provides a clear and unambiguous description of the object's state, which makes it easier to understand what the object represents.

### How to Make `__repr__` Recreatable

To make `__repr__` recreatable, the string it returns should look like a valid Python expression that, when evaluated, would create an identical object. Typically, this means returning a string that resembles a constructor call with the necessary arguments.

#### Example:

Let's consider a simple `Point` class:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
```

In this example, the `__repr__` method returns a string that looks like a valid Python expression: `Point(10, 20)`. This string can be directly evaluated to recreate the `Point` object:

```python
p = Point(10, 20)
print(repr(p))  # Output: Point(10, 20)

# Recreate the object using the repr output
p_recreated = eval(repr(p))  # This will create a new Point(10, 20)
print(p_recreated)           # Output: (10, 20)
```

Here, `eval(repr(p))` takes the string `"Point(10, 20)"`, evaluates it as Python code, and creates a new `Point` object with the same state as the original.

### Important Considerations

1. **Valid Python Expression**: The string returned by `__repr__` should be a valid Python expression. For example, if your object requires more complex initialization (e.g., keyword arguments or nested objects), you need to ensure that the `__repr__` output reflects that.

   ```python
   class Circle:
       def __init__(self, center, radius):
           self.center = center  # Assume center is a Point object
           self.radius = radius

       def __repr__(self):
           return f"Circle(center={repr(self.center)}, radius={self.radius})"

   p = Point(5, 5)
   c = Circle(p, 10)
   print(repr(c))  # Output: Circle(center=Point(5, 5), radius=10)
   ```

   In this case, the `__repr__` of `Circle` includes the `__repr__` of its `center` attribute (which is a `Point` object). This ensures that the entire object hierarchy can be recreated.

2. **Avoid Side Effects**: The `__repr__` method should not have any side effects. It should only return a string representation of the object without modifying the object's state or performing any other actions.

3. **Not Always Possible**: In some cases, it might not be feasible to make `__repr__` fully recreatable. For example, if an object holds references to external resources (like file handles or network connections), it may not be possible to recreate the object exactly from its `__repr__`. In such cases, you can still aim to provide as much detail as possible.

   ```python
   class FileHandler:
       def __init__(self, filename):
           self.filename = filename
           self.file = open(filename, 'r')

       def __repr__(self):
           return f"FileHandler(filename={self.filename})"

   fh = FileHandler("example.txt")
   print(repr(fh))  # Output: FileHandler(filename=example.txt)
   ```

   Here, the `__repr__` doesn't include the file handle itself because it's not possible to recreate an open file handle just from its name. However, it still provides enough information to understand what the object represents.

### Summary

- **Recreatable `__repr__`**: The goal is to make the string returned by `__repr__` a valid Python expression that can recreate the object when evaluated.
- **Use Case**: This is particularly useful for debugging, logging, and ensuring reproducibility of object states.

- **Implementation**: To achieve this, the `__repr__` method should return a string that resembles a constructor call with the necessary arguments. If the object contains other objects, their `__repr__` methods should also be called to ensure the entire object hierarchy can be recreated.

By following these guidelines, you can ensure that your `__repr__` method provides a clear, unambiguous, and useful representation of your objects.


