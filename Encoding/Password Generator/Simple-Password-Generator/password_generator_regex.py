import re
import string
import random

charset = string.ascii_letters + string.digits + "@#$%^&*()_+{}[]:;<>,.?/~\\"
password_regex = re.compile(r'^[0-9a-zA-Z!@#$%^&*()_+{}\[\]:;<>,.?/~\\]{8,50}$')

def generate_new_pass():
    """
    Prompts the user for the desired password length and generates a new password.
    It includes input validation for the password length.
    """
    while True:
        try:
            length = int(input('Enter the length of the password (8-50): '))
            if 8 <= length <= 50:
                new_password = ''.join(random.choice(charset) for _ in range(length))
                return new_password
            else:
                print('Password length must be between 8 and 50 characters.')
        except ValueError:
            print('Invalid input. Please enter a number for the length.')

def validate_password(password):
    """
    Validates a given password against the defined regular expression.
    Returns True if the password is valid, False otherwise.
    """
    return bool(re.match(password_regex, password))

def main():
    """
    The main function of the script. It allows the user to either generate a new
    password or validate an existing one.
    """
    while True:
        choice = input("Choose an action: (1) Generate New Password, (2) Validate Password, (q) Quit: ").lower()

        if choice == '1':
            new_password = generate_new_pass()
            if new_password:
                print(f"Generated password: {new_password}")
        elif choice == '2':
            password_to_validate = input('Enter the password to validate: ')
            if validate_password(password_to_validate):
                length = len(password_to_validate)
                print(f"Password is valid (length: {length}).")
                if 8 <= length < 12:
                    print('Strength: Strong')
                elif length >= 12:
                    print('Strength: Very Strong')
            else:
                print('Password is NOT valid. It must be alphanumeric and between 8-50 characters in length.')
        elif choice == 'q':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter '1', '2', or 'q'.")

if __name__ == '__main__':
    main()