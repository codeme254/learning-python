#!/usr/bin/python3

# if statement is a block of code that will execute if it's condition is true.

age = int(input("How old are you? "))

if age >= 18 and age <= 80:
    print("You are an adult!")
elif age == 100 or age :
    print("You are a senior citizen!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")
