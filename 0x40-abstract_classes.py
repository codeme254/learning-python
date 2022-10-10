#!/usr/bin/python3

# abstract classes prevent a user from creating an object of that class.
# an abstract class is like a ghost class.
# abstract classes are classes that have abstract methods.
# abc means abstract base class
# In other words, a class inheritting an abstract method must provide its own implementation

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        print("stopped")

class Car(Vehicle):
    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

car = Car()
car.go()
# car.stop()
