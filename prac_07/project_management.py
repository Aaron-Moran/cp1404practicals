"""
CP1404/CP5632 Practical - Project Management Program

Estimated: 240 minutes
Actual: 100+45
"""

from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"

def main():
    """Load default data, then print a menu"""
    projects = load_projects(DEFAULT_FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    MENU = (
        "- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit\n"
    )
    choice = input(MENU + ">>> ").lower()
    while choice != "q":
        if choice == "d":
            display_projects(projects)
        elif choice == "l":
            projects = load_projects_prompt(projects)
        elif choice == "s":
            save_projects_prompt(projects)
        else:
            print("Invalid choice")
        choice = input(MENU + ">>> ").lower()

    ask_save_on_quit(projects)

    # TODO Add menu (F/A/U)


def load_projects(filename: str) -> list[Project]:
    """Load projects."""
    projects: list[Project] = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            name, date_text, priority_text, estimate_text, completion_text = line.split("\t")
            start = datetime.strptime(date_text, DATE_FORMAT).date()
            project = Project(name, start, int(priority_text), float(estimate_text), int(completion_text))
            projects.append(project)
    return projects


def save_projects(filename: str, projects: list[Project]) -> None:
    """Save projects to a file with a header row."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for p in projects:
            date_text = p.start_date.strftime(DATE_FORMAT)
            print(f"{p.name}\t{date_text}\t{p.priority}\t{p.estimate}\t{p.completion}", file=out_file)


def load_projects_prompt(current_projects: list[Project]) -> list[Project]:
    """Prompt for a filename and load projects from it; return the new list."""
    filename = input("Load projects from: ")
    new_projects = load_projects(filename)
    print(f"Loaded {len(new_projects)} projects from {filename}")
    return new_projects


def save_projects_prompt(projects: list[Project]) -> None:
    """Prompt for a filename and save projects to it."""
    filename = input("Save projects to: ")
    save_projects(filename, projects)
    print(f"Saved {len(projects)} projects to {filename}")


def ask_save_on_quit(projects: list[Project]) -> None:
    """Ask whether to save to the default file on quit."""
    answer = input(f"Would you like to save to {DEFAULT_FILENAME}? ").strip().lower()
    if answer.startswith("y"):
        save_projects(DEFAULT_FILENAME, projects)
        print(f"Saved {len(projects)} projects to {DEFAULT_FILENAME}")
    print("Thank you for using custom-built project management software.")


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