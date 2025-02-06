Python provides several built-in data structures that allow you to store and manipulate collections of data. The four most commonly used ones are **Lists**, **Sets**, **Dictionaries (Dict)**, and **Tuples**.

# 1. **List**

- _can hold elements of different types, including integers, strings, floats, or even other lists._
- are defined using square brackets `[]`.
- **Ordered**: Elements have a specific order, means position of each element matters.
- **Mutable**: can modify a list by adding, removing, or changing elements.
- **Indexable**: can access elements by their index, starting from `0`.
- **Allows Duplicates**: Lists can contain duplicate elements.

```python
my_list = [1, "apple", 3.14, [2, 3]]
print(my_list[0])  # Output: 1
print(my_list[3][1])  # Output: 3
```

### Common Operations:
- **Accessing Elements**: Use indexing (`my_list[0]`) or slicing (`my_list[1:3]`).
- **Adding Elements**: Use methods like `append()`, `extend()`, or `insert()`.
- **Removing Elements**: Use methods like `remove()`, `pop()`, or `del`.
- **Iterating**: Use a `for` loop to iterate over elements.

### Performance Considerations:
- **Access Time**: Accessing an element by index is **O(1)** _(constant time)._
- **Search Time**: Searching for an element is **O(n)** _(linear time)._
- **Insertion/Deletion**:
  - at the _beginning or middle_ of the list is **O(n)**
  - _appending to the end_ is **O(1)**.

# 2. **Set**

- Sets are defined using curly braces `{}` or the `set()` constructor.
- **Unordered**: Sets do _not maintain any specific order of elements._
- **Unique Elements**: Sets automatically remove duplicates.
- **Mutable**: You can add or remove elements from a set.
- **No Indexing**: Since sets are unordered, you cannot access elements by index.

```python
my_set = {1, 2, 3, 4, 4}  # Duplicate 4 will be removed
print(my_set)  # Output: {1, 2, 3, 4}

# Adding elements
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}
```

### Common Operations:
- **Adding Elements**: `add()` to add a single element, `update()` to add multiple elements.
- **Removing Elements**: `remove()` or `discard()`. `remove()` raises an error if the element doesn't exist, while `discard()` does not.
- **Set Operations**: mathematical set operations like union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`).

### Performance Considerations:
- **Membership Test**: Checking if an element is in a set is **O(1)** on _average_ because sets are implemented as hash tables.
- **Add/Remove**: Adding or removing elements is also **O(1)** on average.
- **Iteration**: Iterating over a set is **O(n)**, where n is the number of elements.

# 3. **Dictionary (Dict)**

A **dictionary** (or `dict`) is an ordered collection of key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any type. Dictionaries are defined using curly braces `{}` with key-value pairs separated by colons `:`.

- **Unordered**: Prior to Python 3.7, dictionaries were unordered. Starting from Python 3.7, dictionaries maintain insertion order (implemented as linked hash map)
- **Key-Value Pairs**: Each element in a dictionary consists of a key and a corresponding value.
- **Mutable**: You can add, remove, or modify key-value pairs.
- **Fast Lookup**: Dictionaries provide fast lookup based on keys because they are implemented as hash tables.

```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Output: Alice

# Adding a new key-value pair
my_dict["profession"] = "Engineer"
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'profession': 'Engineer'}
```

### Common Operations:
- **Accessing Values**: Use the key to access the corresponding value (`my_dict["key"]`).
- **Adding/Updating**: Assign a value to a key to add or update it.
- **Removing Elements**: Use `del my_dict["key"]` or `pop()` to remove a key-value pair.
- **Iterating**: You can iterate over keys, values, or key-value pairs using `keys()`, `values()`, or `items()`.

### Performance Considerations:
- **Lookup Time**: Accessing a value by key is O(1) on average due to hashing.
- **Insertion/Deletion**: Adding or removing key-value pairs is also O(1) on average.
- **Iteration**: Iterating over all keys or values is O(n), where n is the number of key-value pairs.

# 4. **Tuple**

- similar to lists, but once created, their elements cannot be changed.
- defined using parentheses `()`.
- **Ordered**: Like lists, tuples maintain the order of elements.
- **Immutable**: Once a tuple is created, you cannot modify its elements.
- **Indexable**: You can access elements by their index, just like in lists.
- **Allows Duplicates**: Tuples can contain duplicate elements.

```python
my_tuple = (1, "apple", 3.14)
print(my_tuple[1])  # Output: apple

# Trying to modify a tuple will raise an error
# my_tuple[0] = 2  # TypeError: 'tuple' object does not support item assignment
```

### Common Operations:
- **Accessing Elements**: Use indexing (`my_tuple[0]`) or slicing (`my_tuple[1:3]`).
- **Concatenation**: You can concatenate tuples using the `+` operator.
- **Repetition**: You can repeat tuples using the `*` operator.
- **Iterating**: Use a `for` loop to iterate over elements.

### Performance Considerations:
- **Access Time**: Accessing an element by index is O(1) (constant time).
- **Search Time**: Searching for an element is O(n) (linear time).
- **Memory Efficiency**: Tuples are more memory-efficient than lists because they are immutable.

## Summary Table:

| Feature          | List                     | Set                      | Dictionary (Dict)         | Tuple                    |
|------------------|--------------------------|--------------------------|---------------------------|--------------------------|
| **Order**        | Ordered                 | Unordered                | **Ordered** since Python 3.7 | Ordered                 |
| **Mutability**   | Mutable                 | Mutable                  | Mutable                   | Immutable                |
| **Duplicates**   | Allows duplicates       | No duplicates            | Keys are unique           | Allows duplicates        |
| **Indexing**     | Yes                     | No                       | No                        | Yes                      |
| **Performance**  | O(1) for access, O(n) for search | O(1) for membership test | O(1) for key lookup      | O(1) for access, O(n) for search |

## When to Use Each Data Structure?

- **List**: Use when you need an ordered collection of items that may change (mutable). Good for sequences of data where order matters.
- **Set**: Use when you need a collection of unique items and don't care about order. Sets are great for membership testing and eliminating duplicates.
- **Dictionary**: Use when you need to associate keys with values for fast lookups. Dictionaries are ideal for mapping relationships between data.
- **Tuple**: Use when you need an immutable sequence of items. Tuples are useful when you want to ensure that the data cannot be modified.
