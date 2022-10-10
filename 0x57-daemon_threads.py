#!/usr/bin/python3

# daemon thread is a thread that runs in the background and is not important for program to run.
# Your program will not wait for daemon threads to complete before exiting
# non-daemon threads cannot normally be killed, they stay alive until the task is complete

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for {} seconds".format(count))

x = threading.Thread(target=timer, daemon=True)
x.start()
# also
# x.setDaemon(True)
# print(x.isDaemon())

# main thread will be waiting for this statement.
answer = input("Do you want to exit? ")
