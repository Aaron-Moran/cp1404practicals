"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# Ask the user for a score
score = float(input("Enter score: "))

# Check and print the result based on the score
if score < 0:
    print("Invalid score")
elif score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
elif score < 50:
    print("Bad")
else:
    print("Invalid score")