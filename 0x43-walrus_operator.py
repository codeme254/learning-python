#!/usr/bin/python3

# Walrus operator :=
# New in python 3.8, it assigns values to variables as part of a larger expression
happy = True
print(happy)

# Can we just print it directly
print(happy := True)

foods = list()
while True:
    food = input("What food do you like: ")
    if food == "quit":
        break
    foods.append(food)
print(foods)

# with walrus operator
foods = list()

while food := input("What food do you like? ") != "quit":
    foods.append(food)
print(foods)
