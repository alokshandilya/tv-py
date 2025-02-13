# `dataclass` module

- introduced in **Python 3.7**, provides a decorator and functions to automatically generate special methods like `__init__()`, `__repr__()`, `__eq__()`, and others for classes that are primarily used to store data.
  - makes it easier to create clean, readable, and maintainable code when working with classes that are mainly "data containers."

## 1. What Are Dataclasses?

### Purpose

Dataclasses are designed to simplify the creation of classes that are primarily used to store data. They reduce boilerplate code by automatically generating common methods such as:

- `__init__`: Initializes the object.
- `__repr__`: Provides a string representation of the object.
- `__eq__`: Enables equality comparisons between objects.
- `__hash__`: Makes objects hashable (optional).
- `__str__`: Provides a user-friendly string representation.

Instead of manually writing these methods, you can use the `@dataclass` decorator to generate them automatically.

### Advantages

1. **Less Boilerplate Code:** Reduces repetitive code for initializing attributes and defining special methods.
2. **Improved Readability:** Focuses on the data structure rather than boilerplate logic.
3. **Immutability Support:** Supports immutable objects using the `frozen` parameter.
4. **Customization Options:** Allows fine-grained control over how fields are handled.

## 2. Basic Syntax

To use dataclasses, import the `dataclass` decorator from the `dataclasses` module and apply it to your class.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

This is equivalent to:

```python
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) == (other.x, other.y)
        return False
```

## 3. Key Features of Dataclasses

### a. Field Types

You specify the type of each field using type annotations. These annotations are not enforced at runtime but are useful for static type checkers like `mypy`.

#### Example

```python
@dataclass
class Person:
    name: str
    age: int
    height: float
```

### b. Default Values

You can assign default values to fields. Fields with default values must come after fields without defaults.

#### Example

```python
@dataclass
class Book:
    title: str
    author: str
    price: float = 0.0
    in_stock: bool = True
```

### c. Immutable Objects

Use the `frozen=True` parameter to make instances of the class immutable. Attempting to modify an attribute will raise an error.

#### Example

```python
@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float

coords = Coordinates(40.7128, -74.0060)
# coords.latitude = 50  # AttributeError: Cannot assign to field 'latitude'
```

### d. Field Customization

The `field()` function allows you to customize individual fields. For example:

- Exclude fields from `__repr__` or `__eq__`.
- Provide default factory functions for mutable default values.

#### Example

```python
from dataclasses import dataclass, field

@dataclass
class Inventory:
    items: list[str] = field(default_factory=list)  # Avoid mutable default values
    total_value: float = 0.0

inventory = Inventory()
inventory.items.append("apple")
print(inventory)  # Output: Inventory(items=['apple'], total_value=0.0)
```

### e. Post-Initialization Processing

Use the `__post_init__` method to perform additional initialization after the `__init__` method is called.

#### Example

```python
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height

rect = Rectangle(4, 5)
print(rect.area)  # Output: 20
```

## 4. Advanced Features

### a. Inheritance

Dataclasses support inheritance. Subclasses inherit fields and methods from their parent class.

#### Example

```python
@dataclass
class Vehicle:
    brand: str
    model: str

@dataclass
class Car(Vehicle):
    wheels: int = 4

car = Car("Toyota", "Corolla")
print(car)  # Output: Car(brand='Toyota', model='Corolla', wheels=4)
```

### b. Ordering

Use the `order=True` parameter to enable comparison operators (`<`, `<=`, `>`, `>=`) based on the fields.

#### Example

```python
@dataclass(order=True)
class Product:
    name: str
    price: float

p1 = Product("Apple", 1.0)
p2 = Product("Banana", 0.5)
print(p1 > p2)  # Output: True
```

### c. Hashing

By default, dataclasses are unhashable unless `frozen=True`. You can explicitly enable hashing using the `unsafe_hash=True` parameter.

#### Example

```python
@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
print(hash(p1) == hash(p2))  # Output: True
```

## 5. Practical Use Cases

### a. Configuration Classes

Dataclasses are ideal for storing configuration settings.

```python
@dataclass
class Config:
    host: str = "localhost"
    port: int = 8080
    debug: bool = False

config = Config()
print(config)  # Output: Config(host='localhost', port=8080, debug=False)
```

### b. Data Modeling

Use dataclasses to model structured data, such as database records.

```python
@dataclass
class User:
    id: int
    username: str
    email: str
    is_active: bool = True

user = User(1, "alice", "alice@example.com")
print(user)  # Output: User(id=1, username='alice', email='alice@example.com', is_active=True)
```

### c. API Responses

Define types for JSON responses using dataclasses.

```python
@dataclass
class ApiResponse:
    status: str
    data: list[dict]

response = ApiResponse("success", [{"id": 1, "name": "Alice"}])
print(response)  # Output: ApiResponse(status='success', data=[{'id': 1, 'name': 'Alice'}])
```

## 6. Best Practices

1. **Use Type Annotations:** Always annotate fields with types for clarity and compatibility with static type checkers.
2. **Avoid Mutable Defaults:** Use `default_factory` for mutable defaults to avoid shared state issues.
3. **Keep It Simple:** Use dataclasses for simple data structures; avoid adding complex logic.
4. **Immutable When Necessary:** Use `frozen=True` for immutable objects to prevent accidental modifications.
5. **Combine with Other Tools:** Use dataclasses with libraries like `pydantic` for validation or `marshmallow` for serialization.

## 7. Comparison with Named Tuples

| Feature          | Dataclass                      | Named Tuple              |
| ---------------- | ------------------------------ | ------------------------ |
| Mutability       | Mutable (unless `frozen=True`) | Immutable                |
| Default Values   | Supported                      | Not supported            |
| Methods          | Can define custom methods      | Limited to tuple methods |
| Type Annotations | Fully supported                | Limited support          |
| Extensibility    | Highly extensible              | Less flexible            |

## 8. Complete Example

Here’s a complete example combining several features:

```python
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Employee:
    name: str
    age: int
    salary: float = field(default=0.0, compare=False)
    skills: list[str] = field(default_factory=list)

    def add_skill(self, skill: str):
        if not self.skills:  # Frozen objects cannot modify fields
            raise ValueError("Cannot modify skills in a frozen instance")
        self.skills.append(skill)

# Usage
emp1 = Employee("Alice", 30, 50000, ["Python", "SQL"])
emp2 = Employee("Bob", 25, 45000, ["Java", "C++"])

print(emp1)  # Output: Employee(name='Alice', age=30, salary=50000, skills=['Python', 'SQL'])
print(emp1 > emp2)  # Output: True (based on age)
```

## 9. Limitations

1. **No Runtime Type Enforcement:** Type annotations are not enforced at runtime.
2. **Limited to Data-Oriented Classes:** Not suitable for classes with complex behavior or logic.
3. **Performance Overhead:** While minimal, there is some overhead compared to manually written classes.

By mastering dataclasses, you can write clean, concise, and maintainable code for data-oriented tasks. They are particularly useful for configuration management, data modeling, and working with structured data in APIs or databases.
