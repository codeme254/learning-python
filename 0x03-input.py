#!/usr/bin/python3


# accepting user input in function with the input function
name = input("What is your name: ")
print("Your name is: "+name)

age = input("How old are you: ")
# inputs come in as string and if we need to use them as other types, we must convert them.
age = int(age) + 1
print("Your age is: "+str(age))
