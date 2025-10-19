"""
CP1404/CP5632 Practical
Hex colour code lookup
"""

NAME_TO_HEX = {"aliceblue": "#f0f8ff",
               "antiquewhite": "#faebd7",
               "aqua": "#00ffff",
               "coral": "#ff7f50",
               "crimson": "#dc143c",
               "gold": "#ffd700",
               "indigo": "#4b0082",
               "khaki": "#f0e68c",
               "lavender": "#e6e6fa",
               "tomato": "#ff6347"}

def main():
    """Look up hex codes by colour name."""
    print("Known colours:", ", ".join(sorted(NAME_TO_HEX))) # Obsolete in larger dictionaries

    colour_name = input("Colour name: ").strip().lower()
    while colour_name != "":
        try:
            hex_code = NAME_TO_HEX[colour_name]
            print(f"{colour_name} is {hex_code}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Colour name: ").strip().lower()


main()