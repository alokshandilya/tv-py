# Observer Pattern in Python

The Observer pattern is a behavioral design pattern that establishes a one-to-many dependency between objects. When one object (the subject) changes state, all its dependents (observers) are notified and updated automatically.

Here's a detailed explanation with Python implementation:

## Core Components

1. **Subject**: Maintains a list of observers and notifies them of state changes
2. **Observer**: Provides an update interface to receive notifications

## Implementation Example

```python
from abc import ABC, abstractmethod
from typing import List

# Abstract Observer
class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass

# Concrete Subject
class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
        self._state = None

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._state)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self.notify()

# Concrete Observers
class ConcreteObserverA(Observer):
    def update(self, message: str) -> None:
        print(f"Observer A received: {message}")

class ConcreteObserverB(Observer):
    def update(self, message: str) -> None:
        print(f"Observer B received: {message}")
```

## Using the Pattern

```python
# Client code
subject = Subject()

observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)

subject.state = "First state change"
# Output:
# Observer A received: First state change
# Observer B received: First state change

subject.detach(observer_a)
subject.state = "Second state change"
# Output:
# Observer B received: Second state change
```

## Real-world Example: Weather Station

Let's implement a more practical example - a weather station that notifies different displays when weather data changes:

```python
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.state = {"temp": temperature, "humidity": humidity, "pressure": pressure}

class PhoneDisplay(Observer):
    def update(self, data):
        print(f"Phone Display: Temperature: {data['temp']}°C, Humidity: {data['humidity']}%, Pressure: {data['pressure']} hPa")

class WebsiteDisplay(Observer):
    def update(self, data):
        print(f"Website Display: Current conditions - {data['temp']}°C and {data['humidity']}% humidity")
```

## Usage Example

```python
# Using the weather station
weather_station = WeatherStation()

phone_display = PhoneDisplay()
website_display = WebsiteDisplay()

weather_station.attach(phone_display)
weather_station.attach(website_display)

# Weather changes, observers get notified automatically
weather_station.set_measurements(25.2, 65, 1013)
# Output:
# Phone Display: Temperature: 25.2°C, Humidity: 65%, Pressure: 1013 hPa
# Website Display: Current conditions - 25.2°C and 65% humidity
```

## When to Use the Observer Pattern

- When changes to one object require changing other objects, and you don't know how many objects need to change
- When an object should notify other objects without making assumptions about what those objects are
- When you need a loose coupling between interrelated objects

## Benefits

1. **Loose coupling**: Subjects and observers can vary independently
2. **Support for broadcast communication**: One subject can notify multiple observers
3. **Dynamic relationships**: Observers can be added or removed at runtime

## Drawbacks

1. **Memory leaks**: If observers aren't properly detached when no longer needed
2. **Unexpected updates**: Observers might receive notifications at undesirable moments
3. **Cascade of updates**: If observers also act as subjects, it can trigger a cascade of update calls

Would you like me to explain any particular aspect of the Observer pattern in more detail?
