"""
CP1404/CP5632 - Practical 03
files.py
"""

NAME_FILENAME = "name.txt"

# 1. Ask for a name and write it to name.txt
name = input("Enter your name: ")
out_file = open(NAME_FILENAME, "w")
print(name, file=out_file)
out_file.close()