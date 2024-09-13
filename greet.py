# class person with attributes name and age.
# add method greet() that prints a greeting message using the person's name

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello {self.name} your are {self.age} years old")
        
        
person1 =  Person(input("Enter your name: "), int(input("Enter your age: ")))

person1.greet()