#!/usr/bin/python3

# scope of a variable is the region where a variable is recognized.

def display_name():
    name = "code"
    # this is a local variable and it has a local scope
    print(name)

first_name = "zaph";
# this is a global variable
# it is possible to have local and global  versions of a variable
def print_first_name(name):
    first_name = name
    print(first_name)
