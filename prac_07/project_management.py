"""
CP1404/CP5632 Practical - Project Management Program

Estimated: 240 minutes
Actual:
"""

from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects_tests.txt"

def main():
    """Load default data, then print a menu"""
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    MENU = (
        "- (D)isplay projects\n"
        "- (Q)uit\n"
    )
    choice = input(MENU + ">>> ").lower()
    while choice != "q":
        if choice == "d":
            display_projects(projects)
        else:
            print("Invalid choice")
        choice = input(MENU + ">>> ").lower()

    # TODO Add menu (L/S/F/A/U)


def load_projects(filename: str) -> list[Project]:
    """Load projects."""
    projects: list[Project] = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            name, date_text, priority_text, estimate_text, completion_text = line.split("\t")
            start = datetime.strptime(date_text, "%d/%m/%Y").date()
            project = Project(
                name=name,
                start_date=start,
                priority=int(priority_text),
                estimate=float(estimate_text),
                completion=int(completion_text),
            )
            projects.append(project)
    return projects


def display_projects(projects: list[Project]) -> None:
    """Display incomplete and completed projects, each sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


if __name__ == "__main__":
    main()