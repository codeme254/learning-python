#!/usr/bin/python3

# zip(*iterables) aggregate elements from two or more iterables(lists, tuples, sets etc) creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister", "Miss"]
passwords = ["p@ssw0rd", "abc123", "guest", "null"]

users = zip(usernames, passwords)
print(users)
# print(list(users))
for i in users:
    print(i)
users = dict(users)
for key, val in users.items():
    print(key+" : "+val)
