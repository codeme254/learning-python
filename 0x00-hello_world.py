#!/usr/bin/python3

# process finished with exit code 0 means that there were no errors in the program.

# Data types in python, use type() to check the data type
# =======================================================
# string ---> <class 'str'>
name = "Zaphdev"
print(type(name))
first_name = "Zaph"
last_name = "dev"
full_name = first_name + last_name

# numbers ---> <class 'int'>
age = 22
age += 1
age -= 1
age *= 1
print(type(age))
# typecasting variables, in this case integer to string
print("Your age is "+str(age))

# float data type ---> <class 'float'>
# stores numbers that include decimal portion
height = 250.5
print(type(height))

# Boolean data type: True or False ---> <class 'bool'>
human = False
print(type(human))


# Multiple assignment in python
# Allows us to assign multiple variables in the same line in python.
# ==================================================================
name, age, attractive = "Bro", 21, True
num1 = num2 = num3 = num4 = 30
# num1 to num4 have the same values.
