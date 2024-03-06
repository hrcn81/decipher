# Sets and Tuples in Python

## Sets

Sets are a fundamental data type in Python that represent an unordered collection of unique elements. They provide a versatile and efficient way to work with data that requires distinct values.

### Properties of Set

- Sets do not allow duplicate elements.
- Sets are unordered, meaning the elements do not have a specific order.
- Sets are mutable, allowing the addition or removal of elements after creation.
- Sets do not support indexing.

### Common Set Methods

#### Adding Elements:

```python
Set = {1, 2, 3, 4}
Set.add(6)
Set.update([4, 5, 6])
print(Set)
# Output: {1, 2, 3, 4, 5, 6}
```

#### Removing Elements:

```python
Set = {1, 2, 3, 4, 5, 7, 8, 9}
Set.remove(5)
Set.discard(3)
popped_element = Set.pop()
print(Set, f"Popped element is {popped_element}")
# Output: {2, 4, 7, 8, 9} Popped element is 1
```

#### Set Operations:

```python
set1 = {2, 3, 4, 5, 6}
set2 = {4, 5, 7, 9, 1}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set2 - set1
symmetric_diff = set1 ^ set2
print(f"Union set: {union_set}")
print(f"Intersection set: {intersection_set}")
print(f"Difference of sets: {difference_set}")
print(f"Symmetric difference: {symmetric_diff}")
# Output: Union set: {1, 2, 3, 4, 5, 6, 7, 9}
#         Intersection set: {4, 5}
#         Difference of sets: {1, 9, 7}
#         Symmetric difference: {1, 2, 3, 6, 7, 9}
```

#### Other Methods:

```python
Set = {2, 3, 4, 7, 8, 0}
copy_set = Set.copy()
set_length = len(Set)
print("Copy of set", copy_set, "Set length", set_length)
Set.clear()
print("Original set", Set)
# Output: ('Copy of set', set([0, 2, 3, 4, 7, 8]), 'Set length', 6)
#         ('Original set', set([]))
```

#### Membership Check:

```python
Set = {2, 4, 5, 7, 8}
if 5 in Set:
    print("5 is in the set")
# Output: 5 is in the set
```

## Tuples

Tuples are immutable data types in Python, meaning their elements cannot be modified after creation. They are ordered and can contain elements of different data types.

### Access Elements of Tuples

```python
my_tuple = (2, 4, "Python", 5.0, -3)
ele_1 = my_tuple[-2] 
ele_2 = my_tuple[2] 
print(ele_1, ele_2)
# Output: 5.0 Python
```

### Tuple Methods

```python
my_tuple = (1, 3, "Geeks", 4.0, "python", 1)
index = my_tuple.index('python') 
count = my_tuple.count(1) 
print(f"Index of python: {index}, Count of 1: {count}")
# Output: Index of python: 4, Count of 1: 2
```

### Tuple Packing and Unpacking:

```python
packed_tuple = 1, 2, 'three'

# Tuple unpacking
a, b, c = packed_tuple
print(f"Packed Tuple: {packed_tuple}, Unpacked tuple a: {a}, b: {b}, c: {c}")
# Output: Packed Tuple: (1, 2, 'three'), Unpacked tuple a: 1, b: 2, c: three
```

## Challenge Galore

### Problem Statement 1: Two Sum Problem

```python
def two_sum_tuples(nums, target):
    num_indices = {}  

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            return (complement, num)

        num_indices[num] = i

    return None  

nums = [2, 7, 11, 15]
target = 9
result = two_sum_tuples(nums, target)
print("Tuple of Elements:", result)
# Output: Tuple of Elements: (2, 7)
```

### Problem Statement 2: Longest Substring Without Repeating Characters

```python
def length_of_longest_substring(s):
    char_set = set()
    max_length = 0
    left_pointer = 0

    for right_pointer in range(len(s)):
        while s[right_pointer] in char_set:
            char_set.remove(s[left_pointer])
            left_pointer += 1

        char_set.add(s[right_pointer])
        max_length = max(max_length, right_pointer - left_pointer + 1)

    return max_length

input_str = "abcabcbb"
result = length_of_longest_substring(input_str)
print("Length of Longest Substring:", result)
# Output: Length of Longest Substring: 3
```
