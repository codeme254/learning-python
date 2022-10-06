#!/usr/bin/python3

# for loop is a statement that will execute it's block of code a limited amount of times.
# while loop  is unlimited and for loop is limted.

for i in range(10):
    print(i, end=" ")
print("")

for i in range(50, 101, 2):
    print(i, end=" ")
print("")

for i in "Zaphdev":
    print(i, end = " ")
print("")

import time

# starting at 10 and ending at 0
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("*****HAPPY NEW YEAR!*****")
