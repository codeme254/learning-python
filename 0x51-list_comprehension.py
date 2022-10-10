#!/usr/bin/python3

# list comphrension is a way to create a new list with less syntax.
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression if/else for item in iterable]

squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

# comphrension
squares = [i * i for i in range(1, 11)]
print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = [i for i in students if i >= 60]
graded_marks = [i if i >= 60 else "Failed" for i in students]
print(passed_students, graded_marks)
