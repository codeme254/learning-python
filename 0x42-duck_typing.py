#!/usr/bin/python3

# Duck typing is where the class of an object is less important than the methods/attributes that that class might have.
# Class type is not checked if the minimum methods/attributes are present
# If it walks like a duck and it quacks like a duck, then it must be a duck.

class Duck:
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person:
    def catch_duck(self, duck):
        duck.walk()
        duck.talk()
        print("You caught  the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch_duck(duck)
# Even though our parameter is set up to take a duck object, it can also take a chicken object.
person.catch_duck(chicken)
# well, the chicken looks like a duck and that is why it was able to use it.
