"""
CP1404/CP5632 - Practical
randoms.py
"""

# What did you see on line 1?
# 15, 5, 18, 17, 9, 15, 9, 7, 20
# the smallest number was 5 and the largest number was 20

# What did you see on line 2?
# 9, 3, 7, 5, 5, 3, 9, 7, 9, 9, 3
# the smallest number was 3 and the largest number was 9
# cannot produce 4, because step=2 from start=3 only yields odd numbers (3, 5, 7, 9).

# What did you see on line 3?
# 4.08254090906927, 3.5078406005147174, 4.832236141253432, 3.87304479629617, 3.455470577305714, 4.402099021240764
# the smallest number is 2.5 and the largest is 5.5

import random
print(random.randint(1, 100))