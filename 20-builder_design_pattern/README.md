# Builder Design Pattern

- creational design pattern that separates the construction of a complex object from its representation.
  - allows you to construct objects step-by-step and provides more control over the creation process, especially when dealing with objects that require multiple optional parameters or configurations.

## 1. What Is the Builder Design Pattern?

### Purpose

The Builder Pattern is used to construct complex objects by breaking the construction process into smaller, manageable steps. It is particularly useful when:

- An object requires many optional parameters.
- The construction process involves multiple steps or configurations.
- You want to avoid using large constructors with numerous parameters (telescoping constructors).

### Key Characteristics

- **Separation of Concerns:** Decouples the construction of an object from its representation.
- **Step-by-Step Construction:** Allows incremental building of an object.
- **Immutability:** Often used to create immutable objects by setting all properties during construction.
- **Fluent Interface:** Provides a fluent API for chaining method calls.

### Use Cases

- Building complex objects like HTML documents, GUI components, or configuration settings.
- Constructing objects with many optional parameters (e.g., a pizza with customizable toppings).
- Creating immutable objects without exposing their internal state.

## 2. Structure of the Builder Pattern

The Builder Pattern typically involves four components:

1. **Product:**

   - The complex object being constructed.

2. **Builder Interface:**

   - Defines methods for constructing parts of the product.

3. **Concrete Builder:**

   - Implements the builder interface to construct and assemble parts of the product.

4. **Director:**
   - Manages the construction process using the builder interface.

## 3. Implementation

### Example: Building a Pizza

Suppose you are building a system to create pizzas with various toppings, crust types, and sizes. Using the Builder Pattern, you can construct a `Pizza` object step-by-step.

#### Code Example

```python
# Product
class Pizza:
    def __init__(self):
        self.crust = None
        self.size = None
        self.toppings = []

    def __str__(self):
        return f"Pizza with {self.crust} crust, size {self.size}, and toppings: {', '.join(self.toppings)}"

# Builder Interface
class PizzaBuilder:
    def set_crust(self, crust: str):
        pass

    def set_size(self, size: str):
        pass

    def add_topping(self, topping: str):
        pass

    def build(self):
        pass

# Concrete Builder
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_crust(self, crust: str):
        self.pizza.crust = crust
        return self  # Fluent interface

    def set_size(self, size: str):
        self.pizza.size = size
        return self  # Fluent interface

    def add_topping(self, topping: str):
        self.pizza.toppings.append(topping)
        return self  # Fluent interface

    def build(self):
        return self.pizza

# Director (Optional)
class PizzaChef:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def prepare_margherita(self):
        return (
            self.builder.set_crust("thin")
            .set_size("large")
            .add_topping("cheese")
            .add_topping("tomato")
            .build()
        )

# Usage
builder = MargheritaPizzaBuilder()
chef = PizzaChef(builder)

pizza = chef.prepare_margherita()
print(pizza)
# Output: Pizza with thin crust, size large, and toppings: cheese, tomato
```

## 4. Advantages

1. **Improved Readability:** Breaks down complex object creation into smaller, manageable steps.
2. **Flexibility:** Allows dynamic configuration of objects without requiring multiple constructors.
3. **Immutability:** Enables the creation of immutable objects by setting all properties during construction.
4. **Fluent Interface:** Provides a clean and intuitive API for chaining method calls.
5. **Single Responsibility Principle:** Separates the construction logic from the business logic.

## 5. Disadvantages

1. **Increased Complexity:** Introduces additional classes and interfaces, which may be unnecessary for simple objects.
2. **Overhead:** Adds extra layers of abstraction, which may reduce performance slightly.
3. **Learning Curve:** Developers unfamiliar with the pattern may find it harder to understand.

## 6. Practical Use Cases

### a. Building Complex Objects

Construct objects with many optional parameters, such as HTML documents, GUI components, or configuration settings.

#### Example: HTML Document Builder

```python
class HTMLElement:
    def __init__(self, name: str, text: str = ""):
        self.name = name
        self.text = text
        self.elements = []

    def __str__(self, indent: int = 0):
        lines = [" " * indent + f"<{self.name}>"]
        if self.text:
            lines.append(" " * (indent + 2) + self.text)
        for element in self.elements:
            lines.append(element.__str__(indent + 2))
        lines.append(" " * indent + f"</{self.name}>")
        return "\n".join(lines)

class HTMLBuilder:
    def __init__(self, root_name: str):
        self.root = HTMLElement(root_name)

    def add_child(self, child_name: str, child_text: str):
        self.root.elements.append(HTMLElement(child_name, child_text))
        return self  # Fluent interface

    def __str__(self):
        return str(self.root)

# Usage
builder = HTMLBuilder("ul")
builder.add_child("li", "Item 1").add_child("li", "Item 2")
print(builder)
# Output:
# <ul>
#   <li>
#     Item 1
#   </li>
#   <li>
#     Item 2
#   </li>
# </ul>
```

### b. Immutable Object Creation

Create immutable objects by setting all properties during construction.

#### Example: Immutable Configuration

```python
class Configuration:
    def __init__(self, builder):
        self.host = builder.host
        self.port = builder.port
        self.debug = builder.debug

    def __str__(self):
        return f"Configuration(host={self.host}, port={self.port}, debug={self.debug})"

class ConfigurationBuilder:
    def __init__(self):
        self.host = "localhost"
        self.port = 8080
        self.debug = False

    def set_host(self, host: str):
        self.host = host
        return self

    def set_port(self, port: int):
        self.port = port
        return self

    def enable_debug(self):
        self.debug = True
        return self

    def build(self):
        return Configuration(self)

# Usage
builder = ConfigurationBuilder()
config = builder.set_host("example.com").set_port(9090).enable_debug().build()
print(config)
# Output: Configuration(host=example.com, port=9090, debug=True)
```

### c. Game Development

Build game objects (e.g., characters, weapons) with customizable attributes.

## 7. Best Practices

1. **Use Fluent Interfaces:** Return `self` from builder methods to enable method chaining.
2. **Immutable Products:** Ensure the final product is immutable after construction.
3. **Avoid Overusing the Pattern:** For simple objects, direct construction may be sufficient.
4. **Document the Builder Logic:** Clearly document how to use the builder and what each step does.

> particularly useful when dealing with objects that have many optional parameters or require step-by-step configuration.
