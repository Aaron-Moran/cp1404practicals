"""
CP1404/CP5632 - Practical
lists warmup
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = 3, 1, 4, 1, 5, 9 - requires brackets
# numbers[3:4] 1 - requires brackets
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = 3, 1, 4, 1, 5, 9, 2, 6, 5, 3 - requires brackets

numbers[0] = "ten"
print (numbers)

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[-1] = 1
print (numbers)

numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[2:])

numbers = [3, 1, 4, 1, 5, 9, 2]
print(9 in numbers)