#!/usr/bin/python3

# Thread is a flow of execution, like a seperate order of instructions.
# However, each thread takes a turn running to achieve concurrency
# GIL = (Global Interpreter Lock) allows only one thread to hold the control of the Python Interpreter.

import threading
import time
# print the number of threads running in our program
print(threading.active_count())
# we can also get a list of all running threads using the enumerate function
print(threading.enumerate())

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You finished studying")

# calling the three functions within the main thread.
# eat_breakfast()
# drink_coffee()
# study()

# we can run the three functions together
x = threading.Thread(target=eat_breakfast)
# if we had arguments
# x = threading.Thread(target=eat_breakfast, args=(arg1, arg2))
x.start()

y = threading.Thread(target=drink_coffee)
y.start()

z = threading.Thread(target=study)
z.start()
print(threading.active_count())
print(threading.enumerate())

# A thread can wait for other thread to finish before it can execute

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
