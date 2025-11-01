"""
CP1404/CP5632 Practical
wimbledon
Estimate: 30 minutes
Actual: 39 minutes
"""

FILENAME =  "wimbledon.csv"

def main():
    """Load data, process champions and countries, then display results."""
    rows = load_wimbledon_data(FILENAME)

    champion_to_wins = count_champions(rows)
    champion_countries = get_champion_countries(rows)

    print("Wimbledon Champions:")
    for champion in sorted(champion_to_wins):
        print(champion, champion_to_wins[champion])

    countries_line = ", ".join(sorted(champion_countries))
    print()
    print(f"These {len(champion_countries)} countries have won Wimbledon:")
    print(countries_line)


def load_wimbledon_data(filename):
    """
    Load the CSV file into a list of lists, skipping the header.
    """
    rows = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        header = in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) > 6:
                fixed = parts[:5] + [",".join(parts[5:])]
                parts = fixed
            rows.append(parts)
    return rows


def count_champions(rows):
    """Return a dictionary mapping champion name to number of wins."""
    champion_to_wins = {}
    for row in rows:
        champion_name = row[2]
        if champion_name in champion_to_wins:
            champion_to_wins[champion_name] += 1
        else:
            champion_to_wins[champion_name] = 1
    return champion_to_wins


def get_champion_countries(rows):
    """Return a set of country codes for all champions."""
    countries = set()
    for row in rows:
        champion_country = row[1]
        countries.add(champion_country)
    return countries


main()