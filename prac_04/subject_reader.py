"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data(FILENAME)
    print(data, "\n")
    display_subjects(data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(",")
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects

def display_subjects(data):
    """Display subject information as statements"""
    for subject_code, lecturer_name, student_count in data:
        print(f"{subject_code} is taught by {lecturer_name} and has {student_count:3d} students")


main()