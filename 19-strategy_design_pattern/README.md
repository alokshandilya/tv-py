# Strategy Design Pattern

- is a behavioral design pattern that enables selecting an algorithm's behavior at runtime.
  - defines a family of algorithms, encapsulates each algorithm in a separate class, and makes them interchangeable.
  - this allows the client code to choose the appropriate algorithm dynamically without modifying the context.

## 1. What Is the Strategy Design Pattern?

### Purpose

The Strategy Pattern decouples the logic for selecting an algorithm from the logic for executing it. Instead of hardcoding different behaviors into a single class, you encapsulate each behavior in a separate class and allow the client to choose which behavior to use.

### Key Characteristics

- **Encapsulation:** Each algorithm is encapsulated in its own class.
- **Interchangeability:** Algorithms can be swapped at runtime.
- **Open/Closed Principle:** New algorithms can be added without modifying existing code.

### Use Cases

- When you need to define multiple variations of an algorithm (e.g., sorting strategies, payment methods).
- When you want to avoid conditional statements (`if/else` or `switch`) for selecting behavior.
- When you need to make your system more flexible and extensible.

## 2. Structure of the Strategy Pattern

The Strategy Pattern typically involves three components:

1. **Context:**

   - Maintains a reference to a strategy object.
   - Delegates the execution of the algorithm to the strategy.

2. **Strategy Interface:**

   - Defines a common interface for all concrete strategies.

3. **Concrete Strategies:**
   - Implement the strategy interface with specific algorithms.

## 3. Implementation

### Example: Payment Processing System

Suppose you are building a payment processing system that supports multiple payment methods (e.g., credit card, PayPal). You can use the Strategy Pattern to encapsulate each payment method as a separate strategy.

#### Code Example

```python
from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, expiry_date: str, cvv: str):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount: float):
        print(f"Paid ${amount} using Credit Card: {self.card_number}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def pay(self, amount: float):
        print(f"Paid ${amount} using PayPal: {self.email}")

# Context
class ShoppingCart:
    def __init__(self):
        self._payment_strategy = None

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def checkout(self, amount: float):
        if not self._payment_strategy:
            raise ValueError("Payment strategy not set")
        self._payment_strategy.pay(amount)

# Usage
cart = ShoppingCart()

# Use Credit Card Payment
cart.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456", "12/25", "123"))
cart.checkout(100.0)
# Output: Paid $100.0 using Credit Card: 1234-5678-9012-3456

# Use PayPal Payment
cart.set_payment_strategy(PayPalPayment("user@example.com", "password123"))
cart.checkout(50.0)
# Output: Paid $50.0 using PayPal: user@example.com
```

## 4. Advantages

1. **Separation of Concerns:** Encapsulates algorithms in separate classes, making the code easier to maintain and test.
2. **Flexibility:** Allows dynamic switching of algorithms at runtime.
3. **Open/Closed Principle:** New algorithms can be added without modifying existing code.
4. **Eliminates Conditional Statements:** Reduces the need for `if/else` or `switch` statements to select behavior.

## 5. Disadvantages

1. **Increased Complexity:** Introducing multiple classes can make the codebase harder to understand for small projects.
2. **Overhead:** Adds extra layers of abstraction, which may reduce performance slightly.
3. **Learning Curve:** Developers unfamiliar with design patterns may find it harder to grasp the concept.

## 6. Practical Use Cases

### a. Sorting Algorithms

Implement different sorting algorithms (e.g., QuickSort, MergeSort) as strategies and let the client choose the algorithm dynamically.

#### Example

```python
from abc import ABC, abstractmethod

# Strategy Interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list):
        pass

# Concrete Strategies
class QuickSortStrategy(SortStrategy):
    def sort(self, data: list):
        print("Sorting using QuickSort")
        return sorted(data)

class MergeSortStrategy(SortStrategy):
    def sort(self, data: list):
        print("Sorting using MergeSort")
        # Simplified merge sort logic
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

# Context
class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data: list):
        return self._strategy.sort(data)

# Usage
data = [3, 1, 4, 1, 5, 9]
sorter = Sorter(QuickSortStrategy())
print(sorter.sort(data))  # Output: Sorting using QuickSort; [1, 1, 3, 4, 5, 9]

sorter = Sorter(MergeSortStrategy())
print(sorter.sort(data))  # Output: Sorting using MergeSort; [1, 1, 3, 4, 5, 9]
```

### b. Navigation Systems

Implement different navigation strategies (e.g., GPS, offline maps) for a navigation app.

### c. Compression Algorithms

Allow users to choose between different compression algorithms (e.g., ZIP, RAR).

## 7. Best Practices

1. **Keep Strategies Focused:** Each strategy should have a single responsibility.
2. **Use Dependency Injection:** Pass strategies to the context instead of hardcoding them.
3. **Document Behavior:** Clearly document the purpose and usage of each strategy.
4. **Avoid Overusing the Pattern:** For simple cases, direct implementation may be sufficient.

> is particularly useful when you need to support multiple variations of an algorithm or behavior without tightly coupling your code to specific implementations.
