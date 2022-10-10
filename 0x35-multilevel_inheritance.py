#!/usr/bin/python3

# multilevel inherintance in python
# multilevel inheritance is where a child class inherits from another child class.

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
