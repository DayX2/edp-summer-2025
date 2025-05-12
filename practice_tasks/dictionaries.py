
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)

# Accessing values by key
print(person["name"])  # John
print(person.get("age"))  # 30

# Adding a new key-value pair
person["job"] = "Developer"
print(person)

# Updating an existing key
person["age"] = 31
print(person)

# Removing a specific key-value pair
person.pop("city")
print(person)

# Removing the last inserted item (Python 3.7+)
last_item = person.popitem()
print(person)
print("Removed item:", last_item)

# Deleting a specific key
del person["name"]
print(person)

# Clearing the entire dictionary
person.clear()
print(person)  # {}

# Looping through keys
for key in person:
    print(key)

# Looping through values
for value in person.values():
    print(value)

# Looping through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key exists
person = {"name": "Alice", "age": 25}
if "name" in person:
    print("Name is in the dictionary")

# Getting the number of key-value pairs
print(len(person))

# Shallow copy
copy_person = person.copy()
print(copy_person)

# Another way to copy
copy_person_2 = dict(person)
print(copy_person_2)

# Nested dictionary
family = {
    "child1": {"name": "Emma", "age": 5},
    "child2": {"name": "Liam", "age": 8},
    "child3": {"name": "Sophia", "age": 10}
}
print(family)
print(family["child2"]["name"])  # Liam

# Creating a dictionary with the dict constructor
person = dict(name="John", age=30, city="New York")
print(person)
