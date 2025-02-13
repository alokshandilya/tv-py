## 1. Classes in Python

### What is a Class?

- a blueprint for creating objects.
  - defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.
  - encapsulate data and functionality into a single unit.

### Basic Syntax

```python
class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = "I am a class attribute"

    def __init__(self, instance_attribute):
        # Instance attributes (unique to each instance)
        self.instance_attribute = instance_attribute

    def instance_method(self):
        print(f"Instance method called with {self.instance_attribute}")

    @classmethod
    def class_method(cls):
        print(f"Class method called with {cls.class_attribute}")

    @staticmethod
    def static_method():
        print("Static method called")
```

### Key Components

1. **Attributes:**
   - **Class Attributes:** Shared across all instances of the class.
   - **Instance Attributes:** Unique to each instance.
2. **Methods:**
   - **Instance Methods:** Operate on an instance of the class (`self` refers to the instance).
   - **Class Methods:** Operate on the class itself (`cls` refers to the class).
   - **Static Methods:** Do not operate on either the instance or the class; they are utility functions.

#### Example: A Simple Class

```python
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def bark(self):
        print(f"{self.name} says woof!")

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def is_puppy(age):
        return age < 2

# Creating instances
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 1)

# Accessing attributes and methods
print(dog1.name)           # Output: Buddy
dog1.bark()                # Output: Buddy says woof!
print(Dog.get_species())   # Output: Canis familiaris
print(Dog.is_puppy(dog2.age))  # Output: True
```

## 2. Abstract Classes

### What is an Abstract Class?

- a class that cannot be instantiated directly.
  - serves as a blueprint for other classes and enforces certain methods to be implemented by its subclasses.
  - are useful for defining a common interface for a group of related classes.

> Python provides the `abc` module to define abstract classes using the `ABC` class and the `@abstractmethod` decorator.

### Key Characteristics

1. **Cannot Be Instantiated:** You cannot create an object of an abstract class.
2. **Enforces Implementation:** Subclasses must implement all abstract methods defined in the abstract class.
3. **Defines a Contract:** Ensures that subclasses adhere to a specific structure or behavior.

### Syntax

```python
from abc import ABC, abstractmethod

class AbstractClassName(ABC):
    @abstractmethod
    def required_method(self):
        pass  # Subclasses must implement this method

    @abstractmethod
    def another_required_method(self):
        pass  # Subclasses must implement this method
```

#### Example: An Abstract Class

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Subclasses must implement this method

    @abstractmethod
    def move(self):
        pass  # Subclasses must implement this method

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

    def move(self):
        print("Running")

class Bird(Animal):
    def make_sound(self):
        print("Chirp!")

    def move(self):
        print("Flying")

# animal = Animal()  # TypeError: Can't instantiate abstract class Animal
dog = Dog()
dog.make_sound()  # Output: Woof!
dog.move()        # Output: Running

bird = Bird()
bird.make_sound()  # Output: Chirp!
bird.move()        # Output: Flying
```

## 3. Differences Between Classes and Abstract Classes

| Feature               | Regular Class             | Abstract Class                    |
| --------------------- | ------------------------- | --------------------------------- |
| Instantiation         | Can be instantiated       | Cannot be instantiated            |
| Purpose               | Defines concrete behavior | Defines a contract for subclasses |
| Method Implementation | Implements all methods    | May have abstract methods         |
| Use Case              | General-purpose objects   | Base class for polymorphism       |

## 4. Advanced Concepts

### a. Inheritance

- allows one class to inherit attributes and methods from another class.
- derived class can override or extend the behavior of the base class.

#### Example: Inheritance

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"Driving {self.brand} {self.model}")

car = Car("Toyota", "Corolla")
car.start()  # Output: Toyota vehicle started
car.drive()  # Output: Driving Toyota Corolla
```

### b. Polymorphism

- allows objects of different classes to be treated as objects of a common base class.
- often used to achieve polymorphism.

#### Example: Polymorphism

```python
def make_animal_sound(animal):
    animal.make_sound()

dog = Dog()
bird = Bird()

make_animal_sound(dog)   # Output: Woof!
make_animal_sound(bird)  # Output: Chirp!
```

### c. Multiple Inheritance

Python supports multiple inheritance, where a class can inherit from multiple base classes. However, it can lead to complexity (e.g., the "diamond problem"), so it should be used carefully.

#### Example: Multiple Inheritance

```python
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greet()  # Output: Hello from A (Method Resolution Order: A -> B)
```

## 5. Best Practices

1. **Use Abstract Classes for Interfaces:** Define abstract classes when you want to enforce a common interface across subclasses.
2. **Prefer Composition Over Inheritance:** Instead of deep inheritance hierarchies, use composition to build flexible and reusable components.
3. **Keep Classes Focused:** Each class should have a single responsibility (Single Responsibility Principle).
4. **Document Behavior:** Clearly document the purpose of the class, its methods, and any assumptions.
5. **Avoid Overusing Abstract Classes:** Use abstract classes only when necessary; sometimes simple inheritance or interfaces suffice.

## 6. Practical Use Cases

### a. Modeling Real-World Entities

Classes are often used to model real-world entities like cars, animals, or users.

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def send_email(self, message):
        print(f"Sending email to {self.email}: {message}")

user = User("alice", "alice@example.com")
user.send_email("Welcome!")
```

### b. Defining a Plugin System

Abstract classes can define a plugin system where subclasses implement specific functionality.

```python
from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def execute(self):
        pass

class LoggingPlugin(Plugin):
    def execute(self):
        print("Logging data")

class NotificationPlugin(Plugin):
    def execute(self):
        print("Sending notifications")

plugins = [LoggingPlugin(), NotificationPlugin()]
for plugin in plugins:
    plugin.execute()
```

### c. Building a Game Framework

Abstract classes can define the structure of game entities like characters or enemies.

```python
from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

class Warrior(Character):
    def attack(self):
        print("Warrior attacks with a sword")

    def defend(self):
        print("Warrior blocks with a shield")

class Mage(Character):
    def attack(self):
        print("Mage casts a fireball")

    def defend(self):
        print("Mage creates a magical barrier")

characters = [Warrior(), Mage()]
for character in characters:
    character.attack()
    character.defend()
```

Abstract classes are particularly valuable for enforcing contracts and enabling polymorphism, while regular classes provide the foundation for modeling and organizing your code.

Let’s dive into each of these concepts in detail, including their definitions, syntax, use cases, and practical examples. These are fundamental building blocks of object-oriented programming (OOP) in Python.

## What Are Abstract Methods?

- method declared in an abstract base class but does not have an implementation.
- Subclasses must provide an implementation for all abstract methods; otherwise, they remain abstract themselves and cannot be instantiated.

Abstract methods enforce a contract: any subclass inheriting from the abstract class must implement the specified methods.

### Syntax

To define abstract methods, you need to:

1. Import `ABC` (Abstract Base Class) and `abstractmethod` from the `abc` module.
2. Use the `@abstractmethod` decorator to mark a method as abstract.

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def required_method(self):
        pass  # Subclasses must implement this method
```

### Key Characteristics

- Abstract methods cannot have a body (`pass` is used).
- A class with at least one abstract method is considered abstract and cannot be instantiated.
- Subclasses must implement all abstract methods to become concrete (instantiable).

### Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Subclasses must implement this method

    @abstractmethod
    def perimeter(self):
        pass  # Subclasses must implement this method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# shape = Shape()  # TypeError: Can't instantiate abstract class Shape
circle = Circle(5)
print(circle.area())       # Output: 78.5
print(circle.perimeter())  # Output: 31.4
```

## 2. Inheritance

### What Is Inheritance?

Inheritance allows one class (the child or derived class) to inherit attributes and methods from another class (the parent or base class). This promotes code reuse and establishes a hierarchical relationship between classes.

### Types of Inheritance

1. **Single Inheritance:** A class inherits from one base class.
2. **Multiple Inheritance:** A class inherits from multiple base classes.
3. **Multilevel Inheritance:** A class inherits from a derived class, forming a chain.
4. **Hierarchical Inheritance:** Multiple classes inherit from a single base class.
5. **Hybrid Inheritance:** A combination of two or more types of inheritance.

### Syntax

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

child = Child()
child.greet()        # Output: Hello from Parent
child.greet_child()  # Output: Hello from Child
```

### Key Concepts

- **Method Overriding:** A subclass can override a method from the parent class.
- **Super():** Use `super()` to call methods from the parent class.

#### Example: Method Overriding

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Call parent's greet method
        print("Hello from Child")

child = Child()
child.greet()
# Output:
# Hello from Parent
# Hello from Child
```

## 3. Multiple Inheritance

### What Is Multiple Inheritance?

A class can inherit from multiple base classes. This allows the derived class to combine behaviors from multiple sources.

### Syntax

```python
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greet()  # Output: Hello from A (Method Resolution Order: A -> B)
```

### Method Resolution Order (MRO)

Python uses the **C3 Linearization Algorithm** to determine the order in which base classes are searched for methods. You can inspect the MRO using the `mro()` method or `__mro__` attribute.

#### Example: MRO

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

## 4. Private Methods

### What Are Private Methods?

Private methods are methods that are intended to be used only within the class itself. They are prefixed with double underscores (`__`) to make them "private" (name mangling).

### Key Characteristics

- Private methods are not accessible directly from outside the class.
- Name mangling renames the method to `_ClassName__methodName` to avoid accidental access.

### Syntax

```python
class MyClass:
    def public_method(self):
        print("Public method")
        self.__private_method()

    def __private_method(self):
        print("Private method")

obj = MyClass()
obj.public_method()
# Output:
# Public method
# Private method

# obj.__private_method()  # AttributeError: 'MyClass' object has no attribute '__private_method'
```

## 5. Public Methods

### What Are Public Methods?

Public methods are methods that can be accessed from outside the class. By default, all methods in Python are public unless explicitly made private.

### Example

```python
class MyClass:
    def public_method(self):
        print("This is a public method")

obj = MyClass()
obj.public_method()  # Output: This is a public method
```

## 6. Class Methods

### What Are Class Methods?

Class methods are methods bound to the class rather than an instance. They are defined using the `@classmethod` decorator and take `cls` as their first parameter.

### Use Cases

- Factory methods (alternative constructors).
- Methods that operate on class-level data.

### Syntax

```python
class MyClass:
    class_variable = "I am a class variable"

    @classmethod
    def class_method(cls):
        print(f"Class method called with {cls.class_variable}")

MyClass.class_method()  # Output: Class method called with I am a class variable
```

## 7. Static Methods

### What Are Static Methods?

Static methods are methods that do not depend on either the instance (`self`) or the class (`cls`). They are defined using the `@staticmethod` decorator.

### Use Cases

- Utility functions that are logically related to the class but do not require access to instance or class data.

### Syntax

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(5, 3)
print(result)  # Output: 8
```

## Summary Table

| Feature                  | Definition                                                                 | Example Usage                                                   |
| ------------------------ | -------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Abstract Methods**     | Methods without implementation in abstract classes.                        | Enforcing a contract for subclasses.                            |
| **Inheritance**          | Deriving a class from another to reuse or extend functionality.            | Single, multiple, multilevel, hierarchical, hybrid inheritance. |
| **Multiple Inheritance** | A class inherits from multiple base classes.                               | Combining behaviors from multiple sources.                      |
| **Private Methods**      | Methods intended for internal use, prefixed with `__`.                     | Encapsulation and restricting access.                           |
| **Public Methods**       | Methods accessible from outside the class.                                 | Default behavior for methods.                                   |
| **Class Methods**        | Methods bound to the class, not instances, defined with `@classmethod`.    | Factory methods or class-level operations.                      |
| **Static Methods**       | Methods independent of instances or classes, defined with `@staticmethod`. | Utility functions related to the class.                         |
