#!/usr/bin/python3

# we can use programming to mimic real world objects by assigning attributes(what an object is or has) and a method(what an object can do)

# we use classes. capitalized naming convention
# def __init__(self): method is a special method that will construct objects for us
# in other programming languages, it is known as the constructor

class Car:

    def __init__(self, make, model, year, color):
        # attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # methods -> self refers to the object that is using this method
    def drive(self):
        print("This car is driving")
        print("This {} is indeed driving".format(self.model))

    def stop(self):
        print("This car has stopped")



# creating objects from classes
car_1 = Car("Chevy", "Corvette", 2021, "Blue")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()
