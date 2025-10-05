"""
CP1404/CP5632 - Practical 03
files.py
"""

NAME_FILENAME = "name.txt"
NUMBERS_FILENAME = "numbers.txt"

# 1. Ask for a name and write it to name.txt
name = input("Enter your name: ")
out_file = open(NAME_FILENAME, "w")
print(name, file=out_file)
out_file.close()

# 2. Read the name from name.txt and print "Hi {name}!"
in_file = open(NAME_FILENAME, "r")
read_name = in_file.read().strip()
in_file.close()
print(f"Hi {read_name}!")

# 3. Read only the first two numbers from numbers.txt, add and print

# Creates the numbers.txt file with values
NUMBERS_TO_WRITE = [17, 42, 400]
with open(NUMBERS_FILENAME, "w") as out_file:
    for value in NUMBERS_TO_WRITE:
        print(value, file=out_file)

with open(NUMBERS_FILENAME, "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(first_number + second_number)

# 4. Print the total for all lines in numbers.txt
total = 0
with open(NUMBERS_FILENAME, "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)