"""
CP1404/CP5632 Practical
emails
Estimate: 25 minutes
Actual: 27 minutes
"""

def main():
    """Prompt for email, store names, print results"""
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        inferred_name = extract_name_from_email(email) # to be function
        confirmation = input(f"If your name {inferred_name}? (Y/n)").strip().lower()

        if confirmation in ("", "y", "yes"):
            name = inferred_name
        else:
            name =  input("Name: ").strip().title()

        email_to_name[email] = name
        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    """Extract the users name from their email address"""
    local_part = email.split('@', maxsplit = 1)[0]
    spaced = local_part.replace(".", " ").replace("_", " ")
    return spaced.title()


main()