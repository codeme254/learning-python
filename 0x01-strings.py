#!/usr/bin/python3

# useful methods available to us for strings

name = "Bro"
lower_name = "zaphdev"

# length of a string
print(len(name))
# find method -> returns the index of the character passed in.
print(name.find("B"))
# Capitalize -> will only capitalize the first character
print(lower_name.capitalize())
# upper
print(lower_name.upper())
# lower
print(name.lower())
# isdigit() -> returns true or false depending on whether the string is a digit
print(name.isdigit())
# isalpha -> check to see if the string only contains alphabetical orders
print(name.isalpha())
# count -> counts characters passed in the string
print(name.count("o"))
# replace -> replace characters in a string.
print(name.replace("o", "a"))
# print string n times
print(lower_name * 5)
