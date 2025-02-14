# Factory Design Pattern

- a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.
  - promotes loose coupling by eliminating the need to bind application-specific classes into the code. Instead, the code interacts with objects through a common interface.

## 1. What Is the Factory Design Pattern?

### Purpose

The Factory Pattern delegates the responsibility of object creation to a factory class or method, rather than directly instantiating objects in the client code. This makes the system more flexible and easier to extend, as new types of objects can be introduced without modifying existing code.

### Key Characteristics

- **Encapsulation:** The creation logic is encapsulated in a factory class or method.
- **Polymorphism:** Objects are created based on their shared interface or base class.
- **Decoupling:** The client code is decoupled from the concrete implementations of objects.

### Use Cases

- When the exact type of object to be created is determined at runtime.
- When you want to centralize object creation logic to simplify maintenance.
- When you need to create families of related objects without specifying their concrete classes (e.g., Abstract Factory).

## 2. Types of Factory Patterns

There are three main variations of the Factory Pattern:

1. **Simple Factory:** A single factory class creates objects based on input parameters.
2. **Factory Method:** Defines an interface for creating objects but lets subclasses decide which class to instantiate.
3. **Abstract Factory:** Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

## 3. Implementation

### a. Simple Factory

A simple factory is not technically a design pattern but is often used as a precursor to the Factory Method. It uses a single method or class to create objects.

#### Example

```python
from abc import ABC, abstractmethod

# Product Interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Simple Factory
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog")
print(dog.speak())  # Output: Woof!

cat = factory.create_animal("cat")
print(cat.speak())  # Output: Meow!
```

### b. Factory Method

The Factory Method defines an interface for creating objects but lets subclasses decide which class to instantiate. Each subclass implements its own version of the factory method.

#### Example

```python
from abc import ABC, abstractmethod

# Product Interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creator Interface
class AnimalCreator(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

    def get_sound(self):
        animal = self.create_animal()
        return animal.speak()

# Concrete Creators
class DogCreator(AnimalCreator):
    def create_animal(self) -> Animal:
        return Dog()

class CatCreator(AnimalCreator):
    def create_animal(self) -> Animal:
        return Cat()

# Usage
dog_creator = DogCreator()
print(dog_creator.get_sound())  # Output: Woof!

cat_creator = CatCreator()
print(cat_creator.get_sound())  # Output: Meow!
```

### c. Abstract Factory

The Abstract Factory provides an interface for creating families of related or dependent objects without specifying their concrete classes. It is useful when you need to create multiple products that belong to the same family.

#### Example

```python
from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Products
class WindowsButton(Button):
    def render(self):
        return "Rendering a Windows button"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering a Windows checkbox"

class MacOSButton(Button):
    def render(self):
        return "Rendering a MacOS button"

class MacOSCheckbox(Checkbox):
    def render(self):
        return "Rendering a MacOS checkbox"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()

# Client Code
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())

# Usage
windows_factory = WindowsFactory()
client_code(windows_factory)
# Output:
# Rendering a Windows button
# Rendering a Windows checkbox

macos_factory = MacOSFactory()
client_code(macos_factory)
# Output:
# Rendering a MacOS button
# Rendering a MacOS checkbox
```

## 4. Advantages

1. **Loose Coupling:** The client code interacts with objects through interfaces, making it independent of concrete implementations.
2. **Extensibility:** New product types can be added without modifying existing code (Open/Closed Principle).
3. **Centralized Object Creation:** Simplifies maintenance by centralizing the creation logic in one place.
4. **Flexibility:** Allows dynamic creation of objects based on runtime conditions.

## 5. Disadvantages

1. **Increased Complexity:** Introducing factories can make the codebase more complex, especially for small projects.
2. **Overhead:** Adds extra layers of abstraction, which may reduce performance slightly.
3. **Learning Curve:** Developers unfamiliar with design patterns may find it harder to understand the code.

## 6. Practical Use Cases

### a. UI Frameworks

Create platform-specific UI components (e.g., buttons, checkboxes) using the Abstract Factory pattern.

### b. Game Development

Generate different types of game objects (e.g., enemies, weapons) dynamically using the Factory Method.

### c. Dependency Injection

Use factories to provide dependencies to components without hardcoding them.

## 7. Best Practices

1. **Prefer Composition Over Inheritance:** Use factories to compose objects dynamically rather than relying on inheritance hierarchies.
2. **Keep Factories Focused:** Each factory should have a single responsibility (Single Responsibility Principle).
3. **Document the Factory Logic:** Clearly document how objects are created and what variations exist.
4. **Use Dependency Injection When Possible:** For simpler cases, dependency injection can replace the need for factories.

> Whether you use a Simple Factory, Factory Method, or Abstract Factory depends on the complexity of your application and the relationships between objects.
