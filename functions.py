
def greet():
    print("Hello, World!")

greet()

def greet(name):
    print(f"Hello, {name}!")

greet("Ali")
greet("Berke")

def add(a, b):
    return a + b

result = add(3, 5)
print(result)  


def get_person():
    name = "John"
    age = 30
    return name, age

person_name, person_age = get_person()
print(person_name, person_age)


def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person(age=25, name="Ali")

def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))  
print(sum_all(5, 10, 15, 20))  
