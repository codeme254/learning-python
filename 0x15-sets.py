#!/usr/bin/python3

# A set is a collection that is unordered and unindexed. It does not contain any duplicate values.

utensils = {"fork", "spoon", "knife"}
for x in utensils:
    print(x)

# set is faster than a list if you need to check if something exists inside a set

# set methods
# ===============

# add an element
utensils.add("napkin")
print(utensils)

# remove an elemnt
utensils.remove("fork")
print(utensils)

# .clear() removes all elements inside a set.

dishes = {"bowl", "plate", "cup"}

# add one set to another
utensils.update(dishes)
print(utensils)

# we can join two sets together and create an entirely new set.
dinner_table = utensils.union(dishes)
print(dinner_table)

# we can check to see what one set has that the other doesn't.
print(utensils.difference(dishes))

# we can check to see if there is anythin they have in common using the intersection method.
print(utensils.intersection(dishes))
