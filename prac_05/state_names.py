"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania",
                "SA": "South Australia"}
print(CODE_TO_NAME)

code_width = max(len(code) for code in CODE_TO_NAME)
for code in CODE_TO_NAME:
    print(f"{code:<{code_width}} is {CODE_TO_NAME[code]}")

state_code = input("Enter short state: ").strip().upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").strip().upper()