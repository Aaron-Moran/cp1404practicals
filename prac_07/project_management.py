"""
CP1404/CP5632 Practical - Project Management Program

Estimated: 240 minutes
Actual: 100+45+25+30
"""

from datetime import datetime, date
from project import Project

DEFAULT_FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"

MENU = (
    "- (L)oad projects\n"
    "- (S)ave projects\n"
    "- (D)isplay projects\n"
    "- (F)ilter projects by date\n"
    "- (A)dd new project\n"
    "- (U)pdate project\n"
    "- (Q)uit\n"
)

def main():
    """Load default data, then print a menu"""
    projects = load_projects(DEFAULT_FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = input(MENU + ">>> ").lower()
    while choice != "q":
        if choice == "d":
            display_projects(projects)
        elif choice == "l":
            projects = prompt_load_projects()
        elif choice == "s":
            prompt_save_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice")
        choice = input(MENU + ">>> ").lower()

    prompt_save_on_quit(projects)


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


def filter_projects_by_date(projects: list[Project]) -> None:
    """Ask for a date and display projects that start after it, sorted by date."""
    start_after = get_date("Show projects that start after date (dd/mm/yyyy): ")
    filtered = [p for p in projects if p.starts_after(start_after)]
    filtered.sort(key=get_project_start_date)  # sort by date (ascending)
    for p in filtered:
        print(p)


def add_new_project(projects: list[Project]) -> None:
    """Prompt for fields and append a new Project to the list."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    start_date = get_date("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, estimate, completion))


def update_project(projects: list[Project]) -> None:
    """Choose a project, then modify completion % and/or priority (blank to keep)."""
    # Show projects with indices (use current order)
    for i, p in enumerate(projects):
        print(f"{i} {p}")

    index = int(input("Project choice: "))
    project = projects[index]
    print(project)

    new_completion = get_optional_int("New Percentage: ")
    if new_completion is not None:
        project.completion = new_completion

    new_priority = get_optional_int("New Priority: ")
    if new_priority is not None:
        project.priority = new_priority


def get_date(prompt: str) -> date:
    """Prompt for a date string and return a date using DATE_FORMAT."""
    date_text = input(prompt)
    return datetime.strptime(date_text, DATE_FORMAT).date()


def get_project_start_date(project: Project) -> date:
    """Return a project's start date (for sorting)."""
    return project.start_date


def get_optional_int(prompt: str) -> int | None:
    """Return int from input; return None if the user presses Enter."""
    text = input(prompt).strip()
    if text == "":
        return None
    return int(text)


def prompt_load_projects() -> list[Project]:
    """Prompt for a filename and load projects from it; return the new list."""
    filename = input("Load projects from: ")
    new_projects = load_projects(filename)
    print(f"Loaded {len(new_projects)} projects from {filename}")
    return new_projects


def prompt_save_projects(projects: list[Project]) -> None:
    """Prompt for a filename and save projects to it."""
    filename = input("Save projects to: ")
    save_projects(filename, projects)
    print(f"Saved {len(projects)} projects to {filename}")


def prompt_save_on_quit(projects: list[Project]) -> None:
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