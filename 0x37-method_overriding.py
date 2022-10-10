#!/usr/bin/python3

# Method overriding in python
# This is where a child class can provide a specific implementation or another implementation of the parent method.

class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot.")

rabbit = Rabbit()
rabbit.eat()
