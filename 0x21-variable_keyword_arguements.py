#!/usr/bin/python3

# **kwargs is a parameter that will pack all arguements into a dictionary, it is useful in that a function will accept a varying number of keyword arguemts

def hello(**kwargs):
    print("Hello "+kwargs['first'] + " "+kwargs['middle'] + " "+kwargs['last'])

    # iterating throught each key value pair in the dictionary
    for key, val in kwargs.items():
        print(val)

hello(first="jack", middle="the giant", last="slayer")
