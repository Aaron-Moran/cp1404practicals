"""
CP1404/ Practical 2
Password stars
"""
def main():
    # Minimum length of the password
    MIN_PASSWORD_LENGTH = 8

    # Password check loop
    password = input("Password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print("Password is too short!")
        password = input("Password: ")

    print("*" * len(password))
main()