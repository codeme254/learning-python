#!/usr/bin/python3

# *args is a parameter that will  pack all arguements into a tuple, it is useful so that a function can accept a varying amount of arguements.

def add(*args):
    sum = 0
    for number in args:
        sum += number
    return sum
print(add(10, 2, 50))
print(add(23, 11, 80, 33, 55))
