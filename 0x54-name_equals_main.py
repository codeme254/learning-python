#!/usr/bin/python3

# python interpretere sets "special variables" on of which is __name__
# Pyton will assign the __name__ variables a value of __main__ if it's the initial module being run

# By using it, we are checking to see if a user is running the module as a standalone program or they are importing it from another module

import messages
print(__name__) #__main__
print(messages.__name__) #messages

if __name__ == '__main__':
    print("Running the module directly")
else:
    print("Running the module indirectly")
