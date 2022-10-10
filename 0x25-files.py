#!/usr/bin/python3
# file detection in python3
import os

path = "./new_file.sh"

if os.path.exists(path):
    print("That location exists")
    # check if that thing is a file
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location does not exist")
