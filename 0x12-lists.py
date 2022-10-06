#!/usr/bin/python3

# lists are used to store multiple items in a single variable
food = ["pizza", "hamburger", "hotdog", "spaghetti"]

print(food)
# accessed using 0 based indexing
print(food[1])
print(food[2])

# changing elements in a list
food[0] = "sushi"
print(food)

# print all elements in a list using a for loop
for x in food:
    print(x)

# useful methods of a list.

# adding at the end.
food.append("ice cream")
print(food)

# remove an element.
food.remove("hotdog")
print(food)

# remove last element, we use pop
food.pop()
print(food)

# we can also insert at a given index.
food.insert(0, "cake")
print(food)

# sort a list, we use the sort method
food.sort()
print(food)

# we use clear to remove everything in a list
food.clear()
print(food)
