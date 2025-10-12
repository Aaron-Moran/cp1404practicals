"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_records = load_records(FILENAME)
    print(subject_records, "\n")
    display_subjects(subject_records)


def load_records(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(",")
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects

def display_subjects(subject_records):
    """Display subject information as statements"""
    for subject_code, lecturer_name, student_count in subject_records:
        print(f"{subject_code} is taught by {lecturer_name} and has {student_count:3d} students")


main()