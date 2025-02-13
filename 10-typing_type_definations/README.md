- Python is a dynamically typed language, meaning that variable types are inferred at runtime.

  - However, Python also provides tools for **type hinting** and **static type checking**, which allow developers to specify the expected types of variables, function arguments, and return values. This improves code readability, maintainability, and helps catch type-related bugs early.

- The `typing` module in Python is the standard library for type annotations. It provides a rich set of tools for defining complex types, such as generics, unions, and callable signatures. Additionally, third-party libraries like `type_definitions` (or similar libraries) can extend Python's type system with custom or domain-specific types.

## 1. What Is Typing in Python?

### Purpose

Type annotations allow you to specify the expected types of variables, function arguments, and return values. While Python does not enforce these annotations at runtime, they can be used by:

1. **Static Type Checkers:** Tools like `mypy` analyze your code for type correctness.
2. **IDEs and Linters:** Provide better autocompletion, error detection, and code navigation.
3. **Documentation:** Make your code more readable and self-explanatory.

### Basic Syntax

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

age: int = 25
```

- `name: str` specifies that `name` should be a string.
- `-> str` specifies that the function returns a string.
- `age: int` specifies that `age` is an integer.

## 2. The `typing` Module

The `typing` module provides advanced tools for defining complex types. Here are some key features:

### a. Basic Types

These are simple type hints for built-in types:

- `int`, `float`, `str`, `bool`, etc.
- `list`, `dict`, `tuple`, `set`.

#### Example

```python
from typing import List, Dict, Tuple

numbers: List[int] = [1, 2, 3]
person: Dict[str, int] = {"Alice": 25, "Bob": 30}
coordinates: Tuple[float, float] = (40.7128, -74.0060)
```

### b. Generic Types

Generics allow you to define types that work with any data type while maintaining type safety.

#### Example: `List`, `Dict`, `Set`

```python
from typing import List, Dict, Set

def process_items(items: List[str]) -> None:
    for item in items:
        print(item)

def get_user_data() -> Dict[str, int]:
    return {"Alice": 25, "Bob": 30}

unique_numbers: Set[int] = {1, 2, 3}
```

### c. Union Types

Use `Union` to specify that a variable can be one of several types.

#### Example

```python
from typing import Union

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

result = add_numbers(5, 3.5)  # Valid
```

In Python 3.10+, you can use the `|` operator instead of `Union`:

```python
def add_numbers(a: int | float, b: int | float) -> int | float:
    return a + b
```

### d. Optional Types

Use `Optional` to indicate that a value can either be of a specific type or `None`.

#### Example

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

user = find_user(1)  # Returns "Alice"
missing_user = find_user(3)  # Returns None
```

In Python 3.10+, you can use `|` with `None`:

```python
def find_user(user_id: int) -> str | None:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)
```

### e. Callable Types

Use `Callable` to annotate functions or methods.

#### Example

```python
from typing import Callable

def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def add(a: int, b: int) -> int:
    return a + b

result = apply_function(add, 5, 3)  # Output: 8
```

### f. Type Aliases

Use type aliases to simplify complex type definitions.

#### Example

```python
from typing import List, Tuple

Vector = List[float]
Coordinate = Tuple[float, float]

def calculate_distance(point1: Coordinate, point2: Coordinate) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
```

### g. Generics

Use `TypeVar` to define generic types that can work with multiple data types.

#### Example

```python
from typing import TypeVar, List

T = TypeVar('T')  # Generic type

def first_element(lst: List[T]) -> T:
    return lst[0]

numbers = [1, 2, 3]
print(first_element(numbers))  # Output: 1

words = ["hello", "world"]
print(first_element(words))  # Output: hello
```

### h. Protocol (Structural Subtyping)

Protocols allow you to define interfaces based on the structure of objects rather than inheritance.

#### Example

```python
from typing import Protocol

class SupportsAdd(Protocol):
    def __add__(self, other: 'SupportsAdd') -> 'SupportsAdd':
        ...

def add(a: SupportsAdd, b: SupportsAdd) -> SupportsAdd:
    return a + b

print(add(5, 3))  # Output: 8
print(add("Hello, ", "World"))  # Output: Hello, World
```

### i. TypedDict

Use `TypedDict` to define dictionaries with specific key-value types.

#### Example

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

user: User = {"name": "Alice", "age": 25}
print(user["name"])  # Output: Alice
```

### j. Final and Literal

- `Final`: Indicates that a variable or attribute cannot be reassigned.
- `Literal`: Specifies that a value must be one of a fixed set of literals.

#### Example

```python
from typing import Final, Literal

PI: Final[float] = 3.14159
# PI = 3.14  # Error: Cannot reassign a Final variable

def set_mode(mode: Literal["read", "write", "append"]) -> None:
    print(f"Mode set to {mode}")

set_mode("read")  # Valid
# set_mode("delete")  # Error: Argument must be "read", "write", or "append"
```

## 3. Third-Party Libraries for Advanced Typing

While the `typing` module covers most use cases, third-party libraries like `typeguard`, `pydantic`, and `type_definitions` provide additional functionality.

### a. Pydantic

Pydantic enforces type annotations at runtime using validation. It is commonly used for data validation and serialization.

#### Example

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Alice", age=25)
print(user.name)  # Output: Alice
# user = User(name="Alice", age="twenty-five")  # ValidationError
```

### b. Typeguard

Typeguard performs runtime type checking based on type annotations.

#### Example

```python
from typeguard import check_type

def process_number(value: int) -> None:
    check_type("value", value, int)
    print(value)

process_number(42)  # Valid
# process_number("42")  # TypeError
```

### c. Type Definitions

Custom libraries like `type_definitions` (if available) might provide domain-specific types or utilities for working with complex type systems.

## 4. Best Practices

1. **Start Simple:** Begin with basic type hints (`int`, `str`, etc.) and gradually adopt more advanced features.
2. **Use Static Type Checkers:** Tools like `mypy` help catch type errors before runtime.
3. **Document Complex Types:** Use comments or type aliases to clarify complex type definitions.
4. **Be Consistent:** Apply type hints consistently across your codebase.
5. **Avoid Overusing Annotations:** Don’t annotate every single variable unless necessary; focus on public APIs and critical logic.

## 5. Practical Use Cases

### a. API Responses

Define types for JSON responses from APIs using `TypedDict` or `pydantic`.

```python
from typing import TypedDict

class ApiResponse(TypedDict):
    status: str
    data: list[dict]

response: ApiResponse = {
    "status": "success",
    "data": [{"id": 1, "name": "Alice"}]
}
```

### b. Data Validation

Use `pydantic` to validate user input or configuration files.

```python
from pydantic import BaseModel, ValidationError

class Config(BaseModel):
    host: str
    port: int

try:
    config = Config(host="localhost", port=8080)
except ValidationError as e:
    print(e)
```

### c. Function Signatures

Annotate function arguments and return types for clarity.

```python
from typing import List

def sum_of_squares(numbers: List[int]) -> int:
    return sum(x ** 2 for x in numbers)
```

> Type annotations are especially valuable in large projects or when collaborating with others, as they improve code comprehension and reduce errors.
