#!/usr/bin/python3

# a while loop is a statement that will execute a statement as long as it's condition is true.

# while 1 == 1:
#     print("Help! I'm stuck in a loop!")

name = ""
while len(name) == 0:
    name = input("Enter your name: ")
print("Hello "+name)
