import random
import string
import os
import getpass
from dependencies import generate_password
from dependencies import write_password_to_file

# Constants
USER_PWDS_DIR = f'{os.path.dirname(__file__)}/pwds'  # Directory to store generated passwords
print(f'{USER_PWDS_DIR}')
ALPHANUMERIC_CHARS = string.ascii_letters + string.digits + "!@£$%^&*(),."  # Characters for password generation
BASE_NAME = os.path.basename(__file__)  # Get the base name of the current script file
FILE_NAME_STRIP = os.path.splitext(BASE_NAME)[0]  # Remove file extension from the file name

def main():
    if os.path.exists(USER_PWDS_DIR):
        try:
            os.chdir(USER_PWDS_DIR)  # Change the current working directory to the password directory
        except OSError as e:
            print(e)
    else:
        try:
            print(f'Unable to find path {USER_PWDS_DIR}')
            choice = input(f'Would you like to create the directory {USER_PWDS_DIR}? (Y/N): ')
            if choice.lower() in ['y', 'yes']:
                try:
                    print(f'Creating {USER_PWDS_DIR}...')
                    os.mkdir(USER_PWDS_DIR)  # Create the password directory if it doesn't exist
                    if os.path.isdir(USER_PWDS_DIR):
                        print(f'Successfully created: {USER_PWDS_DIR}\n')
                    else:
                        print(f'Unable to create {USER_PWDS_DIR}\n')
                        return
                except OSError as e:
                    print(e)
            else:
                return

        except OSError as e:
            print(e)

    while True:
        try:
            if not os.path.isdir(f'{os.path.dirname(__file__)}/dependencies'):
                os.mkdir(f'{os.path.dirname(__file__)}/dependencies')
            if not os.path.isfile(f'{os.path.dirname(__file__)}/dependencies/__init__.py'):
                with open(f'{os.path.dirname(__file__)}/dependencies/__init__.py', "w") as file:
                    pass

            print(f'\n======================================== {FILE_NAME_STRIP} =======================================')
            num_passwords = input('How many passwords would you like to generate?: ')
            print('')
            if isinstance(num_passwords, int) and int(num_passwords) <= 0 or isinstance(num_passwords, int) and int(num_passwords) >= 20:
                print('You can only generate a positive number of passwords (1-19).')
                continue
            elif num_passwords.lower() in ['del', 'delpwds', 'delete']:
                print('\n========================================WARNING=======================================')
                print('Deleting these passwords is a permanent action there is no way to undo this action.')
                print('========================================WARNING=======================================\n')
                choice = input(f'Are you sure you want to delete the file {USER_PWDS_DIR}? Y/N: ')
                if choice.lower() in ['y', 'yes']:
                    print(f'\nDeleting contents of {USER_PWDS_DIR}...')
                    with open(f'{USER_PWDS_DIR}/pwds.txt', 'w') as file:
                        file.write('')  # Clear the password file
                    if os.path.getsize(f'{USER_PWDS_DIR}/pwds.txt') == 0:
                        print(f'{USER_PWDS_DIR}/pwds.txt has been cleared.\n')
                    else:
                        print(f'Unable to clear {USER_PWDS_DIR}/pwds.txt\n')
            else:
                for _ in range(0, int(num_passwords)):
                    password_length = input('New password length (5-16): ')
                    if password_length.lower() == "exit":
                        break
                    password = generate_password.generate_password(password_length)
                    if password:
                        print('\n==================')
                        print(f'Generated Password: {password}')
                        print('==================\n')
                        write_password_to_file.write_password_to_file(password)
                    else:
                        print('Password length must be between 5 and 16 characters in length. Please try again.')

        except ValueError:
            print('Invalid input. Please enter a valid number of passwords.')

if __name__ == "__main__":
    main()