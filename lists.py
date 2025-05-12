
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing elements by index
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # cherry (last element)

# Slicing a list
print(fruits[1:3])  # ['banana', 'cherry']
print(fruits[:2])   # ['apple', 'banana']
print(fruits[1:])   # ['banana', 'cherry']

# Adding elements to a list
fruits.append("orange")
print(fruits)

# Inserting at a specific index
fruits.insert(1, "blueberry")
print(fruits)

# Removing by value
fruits.remove("banana")
print(fruits)

# Removing by index
removed_fruit = fruits.pop(0)
print(fruits)
print("Removed fruit:", removed_fruit)

# Clearing the list
fruits.clear()
print(fruits)  

# Finding the length of a list
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

# Creating a new list based on an existing one
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares) 

# Sorting a list
fruits = ["cherry", "apple", "banana"]
fruits.sort()
print(fruits)

# Sorting in reverse
fruits.sort(reverse=True)
print(fruits)
