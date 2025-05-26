# Creating a Class and Object

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
#REsult will be "5"

# The __init__ Function (Constructor)

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Result will be "John 36"

# The __str__ Function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
    
p1 = Person("John", 36)
print(p1)

# Result will be "John (36)"

# Object Methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John")
p1.myfunc()

# In here we have a problem because we crated an "age" section but we did not give any value for that

