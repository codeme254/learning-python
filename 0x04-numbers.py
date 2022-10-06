#!/usr/bin/python3

import math

pi = 3.14

# rounds a number for us to the nearest whole number (checks 5 after decimal)
print(round(pi))
print(round(4.8))

# ceil, rounds a number up to the nearest whole integer irregardless of the fractional part
print(math.ceil(pi))
# floor rounds the number down to the nearest whole integer irregardless of the fractional part
print(math.floor(pi))

# abs - prints the absolute value of a number.
print(abs(-50))

# pow will raise a base number to a power
print(pow(pi, 2))

# sqrt finds the square root of a number
print(math.sqrt(64))

# max finds the largest of a varying amount of values
x = 1
y = 2
z = 12
print(max(x, y, z))

# min does the opposite of max
print(min(x, y, z))
