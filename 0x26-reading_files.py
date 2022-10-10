#!/usr/bin/python3

# reading the contents of a file using python
with open('new_file.sh') as file:
    print(file.read())
    # print(file.closed)

# print true if the file is closed or false if the file is still open
print(file.closed)

# it is highly advisable to use the try catch block
try:
    with open('new_file.s') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
