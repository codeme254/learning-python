#!/usr/bin/python3

# tuple is a collection that is ordered and unchangeable, it is used to group together related data.

student = ("Bro", 22, "male", "Bro")

# count the number of times a value appears in a tuple
print(student.count("Bro"))
# get the index of a value in a tuple
print(student.index("male"))

# display all tuple content using a for loop
for x in student:
    print(x)

# check if a value exists in a tuple.
if "Bro" in student:
    print("Bro is here!")

if "zaph" in student:
    print("zaph is here!")
else:
    print("zaph ain't here!")
