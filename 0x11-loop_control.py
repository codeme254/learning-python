#!/usr/bin/python3

# loop control statements are used to change a loop execution from its normal sequence

# break: terminates the loop entirely
# continue: skips to the next iteration of the loop
# pass: does nothing, it just acts as a placeholder.

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
print("")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
