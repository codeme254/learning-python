#!/usr/bin/python3
import random

# generate a random number between 1 and 6
x = random.randint(1, 6)
print(x)

# random number between 0 and 1
y = random.random()
print(y)

my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)
print(z)

# shuffle method shuffles a list or collection
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
