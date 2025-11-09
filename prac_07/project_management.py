"""
CP1404/CP5632 Practical - Project Management Program

Estimated: 240 minutes
Actual: 100+45+25+30+65 = 265 minutes
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
    """Load default data, then run the main menu loop."""
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


def load_projects(filename: str) -> list[Project]:
    """Load projects: Name, Start Date, Priority, Cost Estimate, Completion Percentage."""
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
    start_after = get_valid_date("Show projects that start after date (dd/mm/yyyy): ", DATE_FORMAT)
    filtered = [p for p in projects if p.starts_after(start_after)]
    filtered.sort(key=get_project_start_date)
    for p in filtered:
        print(p)


def add_new_project(projects: list[Project]) -> None:
    """Prompt for fields and append a new Project to the list."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    start_date = get_valid_date("Start date (dd/mm/yyyy): ", DATE_FORMAT)

    priority = get_valid_int("Priority: ")
    while priority is None or priority < 1:
        if priority is None:
            print("This field is required.")
        else:
            print("Invalid input; priority must be greater than 0.")
        priority = get_valid_int("Priority: ")

    estimate = get_valid_float("Cost estimate: $")
    while estimate < 0.0:
        print("Invalid input; estimate must be 0 or greater.")
        estimate = get_valid_float("Cost estimate: $")

    completion = get_valid_int("Percent complete: ")
    while completion is None or completion < 0 or completion > 100:
        if completion is None:
            print("This field is required.")
        else:
            print("Invalid input; completion must be between 0 and 100.")
        completion = get_valid_int("Percent complete: ")

    projects.append(Project(name, start_date, priority, estimate, completion))


def update_project(projects: list[Project]) -> None:
    """Choose a project, then modify completion % and/or priority (blank to keep current value)."""
    for i, p in enumerate(projects):
        print(f"{i} {p}")

    max_index = len(projects) - 1
    index = get_valid_int("Project choice: ")
    while index is None or index < 0 or index > max_index:
        if index is None:
            print("This field is required.")
        else:
            print(f"Invalid input; enter an index between 0 and {max_index}.")
        index = get_valid_int("Project choice: ")

    project = projects[index]
    print(project)

    while True:
        value = get_valid_int("New Percentage: ")
        if value is None:
            break  # keep existing
        if 0 <= value <= 100:
            project.completion = value
            break
        print("Invalid input; enter a value between 0 and 100.")

    while True:
        value = get_valid_int("New Priority: ")
        if value is None:
            break  # keep existing
        if value >= 1:
            project.priority = value
            break
        print("Invalid input; enter an integer greater than 0.")


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


def get_date(prompt: str) -> date:
    """Prompt for a date string and return a date using DATE_FORMAT."""
    date_text = input(prompt)
    return datetime.strptime(date_text, DATE_FORMAT).date()


def get_project_start_date(project: Project) -> date:
    """Return a project's start date (for sorting)."""
    return project.start_date


def get_valid_int(prompt: str) -> int | None:
    """Prompt until a valid integer or blank is entered."""
    while True:
        text = input(prompt).strip()
        if text == "":
            return None
        try:
            return int(text)
        except ValueError:
            print("Invalid input; enter a valid integer.")


def get_valid_float(prompt: str) -> float:
    """Prompt until a valid floating-point number is entered."""
    while True:
        text = input(prompt).strip()
        try:
            return float(text)
        except ValueError:
            print("Invalid input; enter a valid number.")


def get_valid_date(prompt: str, fmt: str) -> date:
    """Prompt until a date parses with the given format."""
    while True:
        text = input(prompt).strip()
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            example = fmt.lower().replace("%d", "dd").replace("%m", "mm").replace("%Y", "yyyy")
            print(f"Invalid date; use format {example}.")

if __name__ == "__main__":
    main()