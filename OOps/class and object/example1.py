class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Creating an object
person1 = Person("Vikas", 25)
person1.greet()
