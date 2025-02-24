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

### Diamond Problem

> The "diamond problem" is a classic issue in object-oriented programming that arises when a class inherits from two classes that have a common ancestor. The problem occurs when the derived class tries to call a method that's defined in the common ancestor, and it's ambiguous which version of the method should be called. Python, like many other languages, has mechanisms to handle this.

Here's a breakdown of the diamond problem and how Python resolves it:

**The Diamond Problem Illustrated**

```
     A
    / \
   B   C
    \ /
     D
```

In this diagram:

- `A` is the base class.
- `B` and `C` both inherit from `A`.
- `D` inherits from both `B` and `C`.

If `A` defines a method `foo()`, and `B` and `C` do _not_ override it, what happens when `D` calls `foo()`? Should it call `A`'s version directly? What if `B` _or_ `C` _did_ override `foo()`? This is the core of the diamond problem.

**Python's Solution: Method Resolution Order (MRO)**

Python uses a mechanism called Method Resolution Order (MRO) to determine the order in which methods are searched for in a class hierarchy. The MRO is a deterministic algorithm that ensures a consistent and predictable way to resolve method calls in complex inheritance scenarios, including the diamond problem.

**How MRO Works (Simplified)**

1. **Depth-First, Left-to-Right:** Python searches the inheritance hierarchy in a depth-first, left-to-right manner. In the diamond example, the search order would generally be: `D`, `B`, `A`, `C`, `A`.

2. **`super()` and Cooperative Inheritance:** Python's `super()` function, when used correctly, plays a key role in making MRO work smoothly. `super()` doesn't just call the parent class's method; it calls the _next method in the MRO_. This enables cooperative inheritance, where classes can collaborate in a predictable way.

3. **C3 Linearization Algorithm:** Python's MRO algorithm is based on the C3 linearization algorithm. This algorithm ensures that the MRO is consistent (preserves the local ordering of classes) and monotonic (if a class `X` precedes a class `Y` in the MRO of class `Z`, then `X` should also precede `Y` in the MRO of any class derived from `Z`).

**Example in Python**

```python
class A:
    def foo(self):
        print("A's foo")

class B(A):
    def foo(self):
        print("B's foo")  # B overrides foo

class C(A):
    pass  # C does not override foo

class D(B, C):
    pass  # D does not override foo

d = D()
d.foo()  # Output: B's foo
print(D.mro()) # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]

```

**Explanation:**

1. `D` inherits from `B` and `C`.
2. `B` overrides `foo()`.
3. `C` does _not_ override `foo()`.
4. When `d.foo()` is called, Python's MRO comes into play.
5. The MRO for `D` is `D`, `B`, `A`, `C`, `A`.
6. The search starts in `D`. `D` doesn't have `foo()`.
7. The search continues in `B`. `B` _does_ have `foo()`.
8. `B`'s `foo()` is executed. The search stops there.

**Key Takeaways**

- Python's MRO (using the C3 algorithm) resolves the diamond problem.
- `super()` enables cooperative inheritance and works seamlessly with MRO.
- Understanding MRO is crucial for working with complex class hierarchies in Python. The `cls.__mro__` attribute or `inspect.getmro(cls)` function will show you the method resolution order for a class.

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

## OOPS concepts in Python

### 1. Encapsulation

Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit (class). It also restricts direct access to some components using access modifiers like private (`__`) or protected (`_`).

#### Example in Python

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):  # Public method to access private data
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300
# print(account.__balance)  # Error: Cannot access private attribute directly
```

- **Key Point:** The `__balance` attribute is encapsulated and can only be accessed or modified through public methods (`deposit`, `withdraw`, `get_balance`).

### 2. Abstraction

Abstraction hides complex implementation details and exposes only the essential features of an object. It allows you to focus on _what_ an object does rather than _how_ it does it.

#### Example in Python

```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method (no implementation)

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"


dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
```

- **Key Point:** The `Animal` class defines an abstract method `make_sound`, which is implemented by its subclasses (`Dog`, `Cat`). The user interacts with the interface without worrying about the implementation.

## 3. Inheritance

Inheritance allows a class (child) to inherit attributes and methods from another class (parent). It promotes code reuse and establishes a hierarchical relationship between classes.

#### Example in Python

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} vehicle started."

class Car(Vehicle):  # Inherits from Vehicle
    def drive(self):
        return f"Driving the {self.brand} car."


car = Car("Toyota")
print(car.start())  # Output: Toyota vehicle started.
print(car.drive())  # Output: Driving the Toyota car.
```

- **Key Point:** The `Car` class inherits the `start` method from the `Vehicle` class and adds its own `drive` method.

### 4. Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different types of objects.

#### Example in Python

```python
class Bird:
    def fly(self):
        return "Bird is flying."

class Airplane:
    def fly(self):
        return "Airplane is flying."

def let_it_fly(flying_object):
    print(flying_object.fly())  # Common interface


bird = Bird()
airplane = Airplane()

let_it_fly(bird)       # Output: Bird is flying.
let_it_fly(airplane)   # Output: Airplane is flying.
```

- **Key Point:** The `let_it_fly` function works with any object that has a `fly` method, demonstrating polymorphic behavior.

### Summary Table

| **Concept**       | **Definition**                                                             | **Python Example**                                                     |
| ----------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Encapsulation** | Bundling data and methods, restricting access to internal details.         | Private attribute `__balance` in `BankAccount`.                        |
| **Abstraction**   | Hiding implementation details, exposing only essential features.           | Abstract class `Animal` with abstract method `make_sound`.             |
| **Inheritance**   | Reusing attributes and methods from a parent class in child classes.       | `Car` class inheriting from `Vehicle`.                                 |
| **Polymorphism**  | Treating objects of different classes as instances of a common superclass. | `let_it_fly` function working with both `Bird` and `Airplane` objects. |

These four principles form the foundation of OOP and are widely used in designing robust, maintainable, and scalable software systems.

## Runtime, Compile time, Method overloading, Method overriding in polymorphism in Python :star2:

### Compile Time vs Runtime

- **Compile Time**: This refers to the phase when the code is being translated into machine code or an intermediate representation (like bytecode in Python). In languages like C++ or Java, a lot of type-checking and method resolution happens at compile time.

  However, **Python is an interpreted language**, meaning there is no separate compilation step as in compiled languages. Instead, Python compiles source code into bytecode on-the-fly, which is then executed by the Python interpreter. So, Python doesn't have a strict "compile time" phase like compiled languages.

- **Runtime**: This is the phase when the program is actually running and executing instructions. In Python, many decisions, such as method resolution and dynamic typing, happen at runtime. This allows for more flexibility but also means that some errors (e.g., type errors) are only caught during execution.

### Method Overloading

**Method overloading** occurs when two or more methods in the same class have the same name but different parameters (either in terms of number of arguments or their types). The correct method to execute is determined at **compile time** based on the arguments passed.

#### Method Overloading in Python:

Python does not support method overloading in the traditional sense (as seen in languages like Java or C++). If you define multiple methods with the same name in a class, the last one defined will override the previous ones.

However, you can simulate method overloading using default arguments or variable-length arguments (`*args` or `**kwargs`).

```python
class Example:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return a

example = Example()
print(example.add(1))          # Output: 1
print(example.add(1, 2))       # Output: 3
print(example.add(1, 2, 3))    # Output: 6
```

> #### 1. Using Default Arguments
>
> One of the simplest ways to simulate method overloading in Python is by using **default arguments**. You can define a single method with default values for some parameters, allowing the method to handle different numbers of arguments.
>
> ```python
> class Example:
>     def add(self, a=None, b=None, c=None):
>         if a is not None and b is not None and c is not None:
>             return a + b + c
>         elif a is not None and b is not None:
>             return a + b
>         elif a is not None:
>             return a
>         else:
>             return 0
>
> example = Example()
> print(example.add(1))          # Output: 1
> print(example.add(1, 2))       # Output: 3
> print(example.add(1, 2, 3))    # Output: 6
> ```
>
> - **Pros**: Simple and easy to implement.
> - **Cons**: Can become cumbersome if you have many possible combinations of arguments.
>
> ### 2. Using Variable-Length Arguments (`*args`)
>
> Another approach is to use **variable-length arguments** (`*args`). This allows you to pass any number of arguments to the method, and then handle them inside the function.
>
> ```python
> class Example:
>     def add(self, *args):
>         total = 0
>         for num in args:
>             total += num
>         return total
>
> example = Example()
> print(example.add(1))          # Output: 1
> print(example.add(1, 2))       # Output: 3
> print(example.add(1, 2, 3))    # Output: 6
> ```
>
> - **Pros**: Flexible and works well when the number of arguments is unknown or varies.
> - **Cons**: Less explicit about the expected arguments, which can make the code harder to understand.
>
> ### 3. Using Keyword Arguments (`**kwargs`)
>
> You can also use **keyword arguments** (`**kwargs`) to simulate method overloading. This allows you to pass named arguments, which can be handled differently based on their names.
>
> ```python
> class Example:
>     def greet(self, **kwargs):
>         if 'name' in kwargs and 'age' in kwargs:
>             return f"Hello {kwargs['name']}, you are {kwargs['age']} years old!"
>         elif 'name' in kwargs:
>             return f"Hello {kwargs['name']}!"
>         else:
>             return "Hello!"
>
> example = Example()
> print(example.greet(name="Alice"))                      # Output: Hello Alice!
> print(example.greet(name="Bob", age=30))               # Output: Hello Bob, you are 30 years old!
> print(example.greet())                                  # Output: Hello!
> ```
>
> - **Pros**: Very flexible and allows for named arguments, making the code more readable.
> - **Cons**: Similar to `*args`, it can become less explicit and harder to manage if overused.
>
> ### 4. Using `@singledispatch` (Single Dispatch Generic Functions) :star2:
>
> Python provides a built-in decorator called `@singledispatch` from the `functools` module, which allows you to define a generic function that behaves differently depending on the type of the first argument. This is a more advanced technique and is useful when you want to overload methods based on the **type** of the arguments.
>
> ```python
> from functools import singledispatch
>
> class Example:
>     @singledispatch
>     def add(self, arg):
>         raise NotImplementedError("Unsupported type")
>
>     @add.register(int)
>     def _(self, arg):
>         return arg
>
>     @add.register(list)
>     def _(self, arg):
>         return sum(arg)
>
>     @add.register(str)
>     def _(self, arg):
>         return arg.upper()
>
> example = Example()
> print(example.add(10))                # Output: 10
> print(example.add([1, 2, 3]))         # Output: 6
> print(example.add("hello"))           # Output: HELLO
> ```
>
> - **Pros**: Clean and elegant, especially when dealing with different types of arguments.
> - **Cons**: Only dispatches based on the type of the first argument, so it's limited in that sense.
>
> ### 5. Using Multiple Dispatch Libraries (e.g., `multipledispatch`) :star2: :star2:
>
> If you need more advanced method overloading that depends on multiple arguments, you can use external libraries like [`multipledispatch`](https://pypi.org/project/multipledispatch/). This library allows you to define multiple versions of a function that behave differently based on the types of all arguments.
>
> First, install the library:
>
> ```bash
> pip install multipledispatch
> ```
>
> Then, you can use it as follows:
>
> ```python
> from multipledispatch import dispatch
>
> class Example:
>     @dispatch(int, int)
>     def add(self, a, b):
>         return a + b
>
>     @dispatch(int, int, int)
>     def add(self, a, b, c):
>         return a + b + c
>
>     @dispatch(str, str)
>     def add(self, a, b):
>         return a + " " + b
>
> example = Example()
> print(example.add(1, 2))              # Output: 3
> print(example.add(1, 2, 3))          # Output: 6
> print(example.add("Hello", "World")) # Output: Hello World
> ```
>
> - **Pros**: Allows method overloading based on the types of multiple arguments.
> - **Cons**: Requires an external library, which may not be desirable in all projects.
>
> ### 6. Using Type Checking with `isinstance()`
>
> Another way to simulate method overloading is by manually checking the types of the arguments using `isinstance()` and handling each case accordingly.
>
> ```python
> class Example:
>     def add(self, a, b=None):
>         if isinstance(a, int) and isinstance(b, int):
>             return a + b
>         elif isinstance(a, str) and isinstance(b, str):
>             return a + " " + b
>         elif b is None:
>             return a
>         else:
>             raise TypeError("Unsupported types")
>
> example = Example()
> print(example.add(1, 2))              # Output: 3
> print(example.add("Hello", "World"))  # Output: Hello World
> print(example.add(10))                # Output: 10
> ```
>
> - **Pros**: Explicitly handles different types of arguments.
> - **Cons**: Can become verbose and hard to maintain if there are many cases.
>
> ### Conclusion: Best Way to Simulate Method Overloading in Python
>
> The **best way** to simulate method overloading in Python depends on your specific use case:
>
> 1. **Simple Cases**: Use **default arguments** or **variable-length arguments** (`*args`, `**kwargs`) for simple scenarios where the number of arguments varies.
> 2. **Type-Based Overloading**: Use **`@singledispatch`** or **`multipledispatch`** when you want to overload methods based on the **type** of arguments.
> 3. **Advanced Scenarios**: For more complex cases where you need to handle multiple types of arguments, consider using **`multipledispatch`** or manual type checking with `isinstance()`.
>
> #### Recommendation:
>
> For most use cases, **default arguments** or **variable-length arguments** (`*args`, `**kwargs`) are sufficient and easy to implement. If you need type-based overloading, `@singledispatch` is a clean and Pythonic solution.

### 3. Method Overriding

**Method overriding** occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The overridden method in the subclass has the same name, return type, and parameters as the method in the parent class. The decision about which method to call is made at **runtime**, based on the object's actual class.

#### Method Overriding in Python:

```python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())

# Output:
# Dog barks
# Cat meows
# Animal speaks
```

In this example:

- The `speak` method is overridden in the `Dog` and `Cat` classes.
- At **runtime**, the correct `speak` method is called based on the actual object type (`Dog`, `Cat`, or `Animal`), demonstrating **runtime polymorphism**.

### 4. **Polymorphism in Python**

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types).

There are two main types of polymorphism:

- **Compile-time polymorphism** (Method overloading): Not natively supported in Python, but can be simulated using default arguments or `*args`/`**kwargs`.
- **Runtime polymorphism** (Method overriding): Achieved through inheritance and method overriding.

#### Example of Polymorphism with Method Overriding:

```python
class Shape:
    def area(self):
        pass  # Abstract method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}")

# Output:
# Area: 78.5
# Area: 24
```

In this example:

- The `area` method is overridden in both `Circle` and `Rectangle` classes.
- At **runtime**, the correct `area` method is called based on the actual object type (`Circle` or `Rectangle`), demonstrating polymorphism.

### Summary

- **Compile Time**: Python doesn't have a strict compile-time phase, but it compiles source code into bytecode before execution.
- **Runtime**: Many decisions, such as method resolution and dynamic typing, occur at runtime in Python.
- **Method Overloading**: Not directly supported in Python, but can be simulated using default arguments or `*args`/`**kwargs`.
- **Method Overriding**: Supported in Python via inheritance. The correct method is resolved at runtime based on the object's actual class.
- **Polymorphism**: Achieved through method overriding, allowing objects of different classes to be treated uniformly through a common interface.

By leveraging these concepts, you can write flexible and reusable code in Python.
