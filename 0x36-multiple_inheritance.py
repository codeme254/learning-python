#!/usr/bin/python3

# multiple inheritance is where a child class is inheriting from more than one parent class.

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# this is the multiple inheritance.
class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
