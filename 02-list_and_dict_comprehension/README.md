# Some important List methods

### 1. **`append(x)`**

- **Description**: Adds an element `x` to the end of the list.
- **Time Complexity**: O(1)

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

---

### 2. **`extend(iterable)`**

- **Description**: Extends the list by appending all elements from the given iterable (e.g., another list).
- **Time Complexity**: O(k), where `k` is the length of the iterable being added.

```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```

---

### 3. **`insert(i, x)`**

- **Description**: Inserts an element `x` at the specified index `i`. Existing elements are shifted to the right.
- **Time Complexity**: O(n), where `n` is the length of the list (due to shifting elements).

```python
my_list = [1, 2, 3]
my_list.insert(1, 10)
print(my_list)  # Output: [1, 10, 2, 3]
```

---

### 4. **`remove(x)`**

- **Description**: Removes the first occurrence of the element `x` from the list. Raises a `ValueError` if the element is not found.
- **Time Complexity**: O(n), as it may need to search through the entire list.

```python
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]

# If the element is not found:
# my_list.remove(5)  # Raises ValueError: list.remove(x): x not in list
```

---

### 5. **`pop([i])`**

- **Description**: Removes and returns the element at index `i`. If no index is provided, it removes and returns the last element.
- **Time Complexity**: O(1) for removing the last element, O(n) for removing from the middle or beginning.

```python
my_list = [1, 2, 3, 4]
popped_element = my_list.pop()
print(popped_element)  # Output: 4
print(my_list)         # Output: [1, 2, 3]

# Remove element at index 1
popped_element = my_list.pop(1)
print(popped_element)  # Output: 2
print(my_list)         # Output: [1, 3]
```

---

### 6. **`clear()`**

- **Description**: Removes all items from the list, making it empty.
- **Time Complexity**: O(1)

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
```

---

### 7. **`index(x[, start[, end]])`**

- **Description**: Returns the index of the first occurrence of element `x`. You can specify optional `start` and `end` parameters to limit the search range. Raises a `ValueError` if the element is not found.
- **Time Complexity**: O(n)

```python
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1

# Search within a specific range
index = my_list.index(2, 2)  # Start searching from index 2
print(index)  # Output: 3
```

---

### 8. **`count(x)`**

- **Description**: Returns the number of times element `x` appears in the list.
- **Time Complexity**: O(n)

```python
my_list = [1, 2, 3, 2, 2]
count = my_list.count(2)
print(count)  # Output: 3
```

---

### 9. **`sort(key=None, reverse=False)`**

- **Description**: Sorts the list in place. You can provide a `key` function to customize the sort order, and set `reverse=True` to sort in descending order.
- **Time Complexity**: O(n log n)

```python
my_list = [3, 1, 4, 1, 5, 9]
my_list.sort()
print(my_list)  # Output: [1, 1, 3, 4, 5, 9]

# Sort in descending order
my_list.sort(reverse=True)
print(my_list)  # Output: [9, 5, 4, 3, 1, 1]

# Custom sorting using a key function
my_list = ["apple", "banana", "cherry"]
my_list.sort(key=len)  # Sort by string length
print(my_list)  # Output: ['apple', 'cherry', 'banana']
```

---

### 10. **`reverse()`**

- **Description**: Reverses the elements of the list in place.
- **Time Complexity**: O(n)

```python
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]
```

---

### 11. **`copy()`**

- **Description**: Returns a shallow copy of the list.
- **Time Complexity**: O(n)

```python
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]

# Modifying the new list does not affect the original list
new_list.append(4)
print(my_list)   # Output: [1, 2, 3]
print(new_list)  # Output: [1, 2, 3, 4]
```

### 12. **`del` Statement**

- **Description**: The `del` statement can be used to remove elements from a list by index or slice.

```python
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Remove element at index 2
print(my_list)  # Output: [1, 2, 4, 5]

# Delete a slice
del my_list[1:3]
print(my_list)  # Output: [1, 5]
```

---

### 13. **`enumerate()`**

- **Description**: While not a list method, `enumerate()` is often used with lists to get both the index and value of each element during iteration.

```python
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: a
# Index: 1, Value: b
# Index: 2, Value: c
```

---

### 14. **`zip()`**

- **Description**: Combines multiple lists into tuples of corresponding elements. Useful for iterating over multiple lists simultaneously.

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```

---

### 15. **`filter()`**

- **Description**: Filters elements from a list based on a condition. Returns an iterator, so you need to convert it back to a list.

```python
my_list = [1, 2, 3, 4, 5]
filtered = filter(lambda x: x > 2, my_list)
print(list(filtered))  # Output: [3, 4, 5]
```

---

### 16. **`map()`**

- **Description**: Applies a function to every item in the list and returns an iterator. You can convert it back to a list.

```python
my_list = [1, 2, 3, 4]
squared = map(lambda x: x**2, my_list)
print(list(squared))  # Output: [1, 4, 9, 16]
```

### List Comprehensions

- **Description**: While not a method, list comprehensions are a powerful way to create lists in a concise manner.

```python
# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

### Slicing (`[:]`)

- **Description**: Slicing allows you to extract a portion of the list. It returns a new list containing the specified elements.

```python
my_list = [1, 2, 3, 4, 5]
sub_list = my_list[1:4]  # Elements from index 1 to 3
print(sub_list)  # Output: [2, 3, 4]

# Reverse a list using slicing
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
```

# Some important Set Methods

### 1. **`add(x)`**

   - **Description**: Adds an element `x` to the set. If the element is already present, it does nothing.
   - **Time Complexity**: O(1) on average.

   ```python
   my_set = {1, 2, 3}
   my_set.add(4)
   print(my_set)  # Output: {1, 2, 3, 4}
   ```

### 2. **`remove(x)`**

   - **Description**: Removes the element `x` from the set. Raises a `KeyError` if the element is not found.
   - **Time Complexity**: O(1) on average.

   ```python
   my_set = {1, 2, 3}
   my_set.remove(2)
   print(my_set)  # Output: {1, 3}

   # If element is not found:
   # my_set.remove(5)  # Raises KeyError: 5
   ```

### 3. **`discard(x)`**

   - **Description**: Removes the element `x` from the set if it is present. Does not raise an error if the element is not found.
   - **Time Complexity**: O(1) on average.

   ```python
   my_set = {1, 2, 3}
   my_set.discard(2)
   print(my_set)  # Output: {1, 3}

   my_set.discard(5)  # No error raised
   print(my_set)  # Output: {1, 3}
   ```

### 4. **`pop()`**

   - **Description**: Removes and returns an arbitrary element from the set. Raises a `KeyError` if the set is empty.
   - **Time Complexity**: O(1) on average.

   ```python
   my_set = {1, 2, 3}
   popped_element = my_set.pop()
   print(popped_element)  # Output: Arbitrary element (e.g., 1)
   print(my_set)          # Output: Remaining elements (e.g., {2, 3})
   ```

### 5. **`clear()`**

   - **Description**: Removes all elements from the set, making it empty.
   - **Time Complexity**: O(1).

   ```python
   my_set = {1, 2, 3}
   my_set.clear()
   print(my_set)  # Output: set()
   ```

### 6. **`copy()`**

   - **Description**: Returns a shallow copy of the set.
   - **Time Complexity**: O(n), where `n` is the size of the set.

   ```python
   my_set = {1, 2, 3}
   new_set = my_set.copy()
   print(new_set)  # Output: {1, 2, 3}
   ```

### 7. **`union(*others)` or `|`**

   - **Description**: Returns a new set containing all elements from the original set and all other sets provided.
   - **Time Complexity**: O(n + k), where `n` is the size of the original set and `k` is the size of the other sets.

   ```python
   set_a = {1, 2, 3}
   set_b = {3, 4, 5}
   union_set = set_a.union(set_b)
   print(union_set)  # Output: {1, 2, 3, 4, 5}

   # Using the | operator
   union_set = set_a | set_b
   print(union_set)  # Output: {1, 2, 3, 4, 5}
   ```

### 8. **`intersection(*others)` or `&`**

   - **Description**: Returns a new set containing only the elements that are common to all sets.
   - **Time Complexity**: O(min(n, k)), where `n` and `k` are the sizes of the sets.

   ```python
   set_a = {1, 2, 3}
   set_b = {3, 4, 5}
   intersection_set = set_a.intersection(set_b)
   print(intersection_set)  # Output: {3}

   # Using the & operator
   intersection_set = set_a & set_b
   print(intersection_set)  # Output: {3}
   ```

### 9. **`difference(*others)` or `-`**

   - **Description**: Returns a new set containing elements that are in the original set but not in the other sets.
   - **Time Complexity**: O(n), where `n` is the size of the original set.

   ```python
   set_a = {1, 2, 3}
   set_b = {3, 4, 5}
   difference_set = set_a.difference(set_b)
   print(difference_set)  # Output: {1, 2}

   # Using the - operator
   difference_set = set_a - set_b
   print(difference_set)  # Output: {1, 2}
   ```

### 10. **`symmetric_difference(other)` or `^`**

   - **Description**: Returns a new set containing elements that are in either of the sets but not in both.
   - **Time Complexity**: O(n + k), where `n` and `k` are the sizes of the sets.

   ```python
   set_a = {1, 2, 3}
   set_b = {3, 4, 5}
   sym_diff_set = set_a.symmetric_difference(set_b)
   print(sym_diff_set)  # Output: {1, 2, 4, 5}

   # Using the ^ operator
   sym_diff_set = set_a ^ set_b
   print(sym_diff_set)  # Output: {1, 2, 4, 5}
   ```

### 11. **`isdisjoint(other)`**

   - **Description**: Returns `True` if the set has no elements in common with the other set.
   - **Time Complexity**: O(min(n, k)).

   ```python
   set_a = {1, 2, 3}
   set_b = {4, 5, 6}
   print(set_a.isdisjoint(set_b))  # Output: True

   set_c = {3, 4, 5}
   print(set_a.isdisjoint(set_c))  # Output: False
   ```

### 12. **`issubset(other)` or `<=`**

   - **Description**: Returns `True` if all elements of the set are in the other set.
   - **Time Complexity**: O(n), where `n` is the size of the set.

   ```python
   set_a = {1, 2}
   set_b = {1, 2, 3, 4}
   print(set_a.issubset(set_b))  # Output: True

   # Using the <= operator
   print(set_a <= set_b)  # Output: True
   ```

### 13. **`issuperset(other)` or `>=`**

   - **Description**: Returns `True` if all elements of the other set are in the original set.
   - **Time Complexity**: O(k), where `k` is the size of the other set.

   ```python
   set_a = {1, 2, 3, 4}
   set_b = {1, 2}
   print(set_a.issuperset(set_b))  # Output: True

   # Using the >= operator
   print(set_a >= set_b)  # Output: True
   ```

# Some important (Dict) Methods

### 1. **`get(key[, default])`**

   - **Description**: Returns the value for the specified key. If the key is not found, it returns the default value (or `None` if no default is provided).
   - **Time Complexity**: O(1) on average.

   ```python
   my_dict = {'a': 1, 'b': 2}
   print(my_dict.get('a'))  # Output: 1
   print(my_dict.get('c', 0))  # Output: 0 (default value)
   ```

### 2. **`keys()`**

   - **Description**: Returns a view object that displays a list of all the keys in the dictionary.
   - **Time Complexity**: O(1).

   ```python
   my_dict = {'a': 1, 'b': 2}
   print(my_dict.keys())  # Output: dict_keys(['a', 'b'])
   ```

### 3. **`values()`**

   - **Description**: Returns a view object that displays a list of all the values in the dictionary.
   - **Time Complexity**: O(1).

   ```python
   my_dict = {'a': 1, 'b': 2}
   print(my_dict.values())  # Output: dict_values([1, 2])
   ```

### 4. **`items()`**

   - **Description**: Returns a view object that displays a list of `(key, value)` tuple pairs.
   - **Time Complexity**: O(1).

   ```python
   my_dict = {'a': 1, 'b': 2}
   print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2)])
   ```

### 5. **`pop(key[, default])`**

   - **Description**: Removes and returns the value associated with the key. If the key is not found, it returns the default value (or raises a `KeyError` if no default is provided).
   - **Time Complexity**: O(1) on average.

   ```python
   my_dict = {'a': 1, 'b': 2}
   value = my_dict.pop('a')
   print(value)  # Output: 1
   print(my_dict)  # Output: {'b': 2}

   # With default value
   value = my_dict.pop('c', 0)
   print(value)  # Output: 0
   ```

### 6. **`popitem()`**

   - **Description**: Removes and returns the last inserted `(key, value)` pair as a tuple. Raises a `KeyError` if the dictionary is empty.
   - **Time Complexity**: O(1).

   ```python
   my_dict = {'a': 1, 'b': 2}
   item = my_dict.popitem()
   print(item)  # Output: ('b', 2)
   print(my_dict)  # Output: {'a': 1}
   ```

### 7. **`update([other])`**

   - **Description**: Updates the dictionary with key-value pairs from another dictionary or iterable of `(key, value)` pairs.
   - **Time Complexity**: O(k), where `k` is the number of items being added.

   ```python
   my_dict = {'a': 1, 'b': 2}
   my_dict.update({'c': 3, 'd': 4})
   print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
   ```

### 8. **`setdefault(key[, default])`**

   - **Description**: Returns the value of the key if it exists. If the key does not exist, it inserts the key with the specified default value and returns the default value.
   - **Time Complexity**: O(1) on average.

   ```python
   my_dict = {'a': 1, 'b': 2}
   value = my_dict.setdefault('c', 3)
   print(value)  # Output: 3
   print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
   ```

### 9. **`clear()`**

   - **Description**: Removes all items from the dictionary.
   - **Time Complexity**: O(1).

   ```python
   my_dict = {'a': 1, 'b': 2}
   my_dict.clear()
   print(my_dict)  # Output: {}
   ```

### 10. **`copy()`**

   - **Description**: Returns a shallow copy of the dictionary.
   - **Time Complexity**: O(n), where `n` is the size of the dictionary.

   ```python
   my_dict = {'a': 1, 'b': 2}
   new_dict = my_dict.copy()
   print(new_dict)  # Output: {'a': 1, 'b': 2}
   ```

11. **`fromkeys(iterable[, value])`**

    - **Description**: Creates a new dictionary with keys from the iterable and values set to the specified value (or `None` by default).
    - **Time Complexity**: O(n), where `n` is the length of the iterable.

    ```python
    keys = ['a', 'b', 'c']
    new_dict = dict.fromkeys(keys, 0)
    print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
    ```


# Some important Tuple Methods

Tuples are immutable, so they have fewer methods compared to lists, sets, and dictionaries. However, there are still a few useful methods:

1. **`count(x)`**

   - **Description**: Returns the number of times `x` appears in the tuple.
   - **Time Complexity**: O(n), where `n` is the length of the tuple.

   ```python
   my_tuple = (1, 2, 3, 2, 4, 2)
   count = my_tuple.count(2)
   print(count)  # Output: 3
   ```

2. **`index(x[, start[, end]])`**

   - **Description**: Returns the index of the first occurrence of `x`. You can specify optional `start` and `end` parameters to limit the search range. Raises a `ValueError` if the element is not found.
   - **Time Complexity**: O(n), where `n` is the length of the tuple.

   ```python
   my_tuple = (1, 2, 3, 2, 4)
   index = my_tuple.index(2)
   print(index)  # Output: 1

   # Search within a specific range
   index = my_tuple.index(2, 2)
   print(index)  # Output: 3
   ```
