#!/usr/bin/python3

# filter() creates a collection of elements from an iterable which a function returns true
# filter(function, iterable)

friends = [
("Rachel", 19),
("Monica", 18),
("Phoebe", 17),
("Joey", 16),
("Chandler", 21),
("Ross", 20)
]
age = lambda data: data[1] >= 18
drinking_buddies = list(filter(age, friends))
print(drinking_buddies)
