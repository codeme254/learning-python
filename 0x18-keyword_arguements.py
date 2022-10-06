#!/usr/bin/python3

# these are arguements that are preceeded by identifier when calling a function, their order does not matter.

def hello(first, middle, last):
    print("Hello {} {} {}".format(first, middle, last))

hello(middle="Dennis", last="zaph", first="otwoma")
