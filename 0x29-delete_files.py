#!/usr/bin/python3

import os

# os.remove('tmpfile1')

try:
    os.remove('tmpfile2')
except FileNotFoundError:
    print("That file was not found: Maybe it is already deleted")


# os.rmdir() removes an empty directory
# os.rmtree() removes an entire directory
