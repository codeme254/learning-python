#!/usr/bin/python3

# sort() method is used with lists
# sort() functions is used with iterables including lists

students = ["Jack", "Hocus", "Potter", "Daenerys"]
students.sort()
for i in students:
    print(i)

# sorting the list in descending order, default is ascending
students.sort(reverse=True)
for i in students:
    print(i)

students = ("Jane", "Rick", "Glenn", "Maggie", "Darrel")
sorted_students = sorted(students)
print(sorted_students)
# sorting in reverse order,
sorted_students = sorted(students, reverse=True)
print(sorted_students)

# ================================
students = [
["Rick", "F", 60],
["Sandy", "A", 33],
["Patrick", "D",  36],
["Glenn", "B", 55]
]

# sorting based on key
grade = lambda grades: grades[1]
students.sort(key=grade)
for i in students:
    print(i)
