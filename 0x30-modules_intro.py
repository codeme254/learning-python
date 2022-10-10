#!/usr/bin/python3

# a module is a file containing python code.
# It may contain classes, etc which are used with modular programming.
# the idea is to seperate your program into parts.

# import messages
#
# messages.hello()
# messages.bye()

# from messages import hello, bye
# hello()
# bye()
import messages as msg
msg.hello()
msg.bye()

help('modules')
