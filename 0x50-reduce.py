#!/usr/bin/python3

# reduce applies a function to an iterabel and reduces it to a single cumulative value.
# It performs the function on the first two elements and repeats the process until 1 value remains

# reduce(function, iterable)

import functools
letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x + y, letters)
print(word)
