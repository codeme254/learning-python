#!/usr/bin/python3

# an exception is an event detected during execution that interrupt the flow of a program.
# its a good practice to handle specific exceptions as they occur.

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    # print(result)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError as e:
    # additional way to handle exception
    print(e)
    print("Enter only numbers please")
except Exception:
    print("something went wrong")
else:
    print(result)
finally:
    # whether or not we catch an exception, this block will always be executed
    print("Thanks for using our calculator thoug.")
