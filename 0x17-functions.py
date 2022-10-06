#!/usr/bin/python3

#  function is a block of code which is only executed when called
# this process is also known as invoking a function.
def hello():
    print("Hello!")
hello()

# functions with parameters
def sayHello(name):
    print("Hello: "+name)
sayHello("zaph")

def greetCustom(name, greeting):
    print(greeting + " "+name)
greetCustom("zaph", "hello")

# return statement in python.
# used to send values/objects back to the caller.

def multiply(a, b):
    return a * b
print(multiply(5, 5))
def add(a, b):
    result = a + b
    return result
