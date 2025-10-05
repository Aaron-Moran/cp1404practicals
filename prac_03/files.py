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
with open(NUMBERS_FILENAME, "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(first_number + second_number)