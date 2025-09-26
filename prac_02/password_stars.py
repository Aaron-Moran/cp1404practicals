"""
CP1404/ Practical 2
Password stars
"""
def main():
    # Minimum length of the password
    MIN_PASSWORD_LENGTH = 8

    # Password check loop
    password = get_password()
    while len(password) < MIN_PASSWORD_LENGTH:
        print("Password is too short!")
        password = get_password()

    print("*" * len(password))

def get_password() -> str:
    password = input("Password: ")
    return password

main()