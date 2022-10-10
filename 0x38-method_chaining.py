#!/usr/bin/python3

# Method chaining in python

# Method chaining is used to call multiple methods sequentially.
# each call performs an action on the same object and returns self.
# You always return self from the methods if you want to use method chaining

class Car:
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("Yous step on the break")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()
car.turn_on()
car.drive()
car.brake()
car.turn_off()

# method chaining
car.turn_on().drive().brake().turn_off()
