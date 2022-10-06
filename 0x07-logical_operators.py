#!/usr/bin/python3

# logical operators are used to check two or more conditional statements
# they are and, or, not
temp = int(input("What is the temperature outside: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today!")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("the temperature is bad today!")
    print("stay inside!")
elif not(temp == 100):
    print("the temperature is not 100 degrees celsius!")
