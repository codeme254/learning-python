#!/usr/bin/python3

import time

# epoch = date and time from which a computer measure system time.
print(time.ctime(0)) #converts time expressed in seconds since epoch to a readable string.
# epoch in short is when your computer thinks time began or the reference point.

# return seconds passed since epoch
print(time.time())

# localtime() gets the current time
# it returns a time object in year, day. hour, minute etc
# we can use strftime() to format the output
print(time.localtime())
time_object = time.localtime()
print(time.strftime("%B %d %Y %H: %M: %S", time_object))

# getting utc i.e Coordinated Universal Time.
time_object = time.gmtime()
print(time_object)

# strptime passes a string representation of a time or day and returns a time object
time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

# asctime acepts a time object or a tuple representation of a relative time.
time_tuple = (202, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

# mktime takes tuple representation of a time object and converts into seconds
