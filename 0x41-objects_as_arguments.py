#!/usr/bin/python3

# objects as arguments

class Car:
    color = None

# function that accepts the object as argument
def change_color(car, color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1, "red")
change_color(car_2, "White")
change_color(car_3, "blue")

print(car_1.color)
print(car_2.color)
print(car_3.color)
