import random
import string
import os
import getpass

# Constants
USER_PWDS_DIR = f'{os.path.dirname(__file__)}/pwds'  # Directory to store generated passwords
print(f'{USER_PWDS_DIR}')
ALPHANUMERIC_CHARS = string.ascii_letters + string.digits + "!@£$%^&*(),."  # Characters for password generation
BASE_NAME = os.path.basename(__file__)  # Get the base name of the current script file
FILE_NAME = os.path.basename(BASE_NAME)  # Get the file name from the base name
FILE_NAME_STRIP = os.path.splitext(FILE_NAME)[0]  # Remove file extension from the file name

def generate_password(length):
    """
    Generates a random password of the specified length.

    Args:
        length (int): The length of the password to generate.

    Returns:
        str: The generated password or None if the input is invalid.
    """
    try:
        length = int(length)
        if 5 <= length <= 16:
            return ''.join(random.choice(ALPHANUMERIC_CHARS) for _ in range(length))
        else:
            return None
    except ValueError:
        return None