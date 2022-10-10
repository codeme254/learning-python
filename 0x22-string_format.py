#!/usr/bin/python3

# str.format() optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item))

# positional arguement
print("The {0} jumped over the {1}".format(animal, item))
# keyword arguement
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))

# padding a string when displaying when using the format method
name = "zaphdev"
print("Hello, my name is {}. Nice to meet you".format(name))
# Hello, my name is zaphdev. Nice to meet you
print("Hello, my name is {:10}. Nice to meet you".format(name))
# Hello, my name is zaphdev   . Nice to meet you

# You can left align using < sign. Hard to see since it is the default
print("Hello, my name is {:<10}. Nice to meet you".format(name))
# Hello, my name is zaphdev   . Nice to meet you

# right aligning using > sign. 10 spaces before
print("Hello, my name is {:>10}. Nice to meet you".format(name))
# Hello, my name is    zaphdev. Nice to meet you

# center align using the caret ^
print("Hello, my name is {:^10}. Nice to meet you".format(name))
# Hello, my name is  zaphdev  . Nice to meet you


# formatting numbers
number = 3.14159

# displaying only the first two digits after the decimal/rounding the number
print("The number is {:.2f}".format(number))

# putting a comma inside the number.
number = 1000000000
print("The earning is {:,}".format(number))
# The earning is 1,000,000,000

# print the binary representation using b.
print("{} in binary is {:b}".format(number, number))
# 1000000000 in binary is 111011100110101100101000000000
# octal is o and and hexadecimal is x.
# use e for scientific notation.
