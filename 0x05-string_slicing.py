#!/usr/bin/python3

# slicing is used to create a substring by extracting elements from another string.
# we use indexing or slice() to do slicing in python.

# INDEXING.
# =========
# [start:stop:step]

name = "Bro Code"
first_name = name[0:3] #Bro
print(first_name)
# stopping index is not included
# we can omit the starting index
print(first_name[:3])

last_name = name[4:8]
print(last_name)
# we can omit the last index to denote slicing to the end
print(name[4:])

# using the step option
funky_name = name[0:8:2]
print(funky_name) # BoCd


# reversing a string in python
reversed_name = name[::-1]
print(reversed_name)


# using the slice function.
# also takes start stop and step
website = "http://wikipidea.com"
slice = slice(7, -4)
print(website[slice])
