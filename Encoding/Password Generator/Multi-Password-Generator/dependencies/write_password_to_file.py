import random
import string
import os
import getpass

# Constants
USER_PWDS_DIR = f'{os.path.dirname(os.path.dirname(__file__))}/pwds'  # Directory to store generated passwords
ALPHANUMERIC_CHARS = string.ascii_letters + string.digits + "!@£$%^&*(),."  # Characters for password generation
BASE_NAME = os.path.basename(__file__)  # Get the base name of the current script file
FILE_NAME = os.path.basename(BASE_NAME)  # Get the file name from the base name
FILE_NAME_STRIP = os.path.splitext(FILE_NAME)[0]  # Remove file extension from the file name

def write_password_to_file(password):
    """
    Writes a password to a file or creates the file if it doesn't exist.

    Args:
        password (str): The password to write to the file.
    """
    try:
        if os.path.isfile(f'{USER_PWDS_DIR}/pwds.txt'):
            with open(f'{USER_PWDS_DIR}/pwds.txt', "a") as file:
                file.write(f'{password}\n')  # Append the password to the file if it exists
        else:
            create_file = input(f'No such file {USER_PWDS_DIR}/pwds.txt. Would you like to create one? (Y/N): ')
            if create_file.lower() in ['y', 'yes']:
                with open(f'{USER_PWDS_DIR}/pwds.txt', "w") as file:
                    file.write(f'{password}\n')  # Create the file and write the password

    except OSError as e:
        print(e)