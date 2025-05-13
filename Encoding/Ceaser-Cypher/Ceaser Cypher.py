# Importing necessary modules
import os  # For interacting with the operating system, like checking if a file exists.
import string  # Provides useful string constants, like uppercase and lowercase letters.

base_rotation = 'A-MN-Za-mn-z'

# Defines the path to the file that will be read and encrypted, relative to the script's directory.
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script.
file = os.path.join(script_dir, 'data.txt')  # Construct the relative path to 'data.txt'.

def rotate_char(char, number):
    """
    Rotates a single alphabetic character by a specified number of positions.
    Non-alphabetic characters are returned unchanged.

    Args:
        char (str): The single character to rotate.
        number (int): The number of positions to rotate the character.

    Returns:
        str: The rotated character, or the original character if it's not a letter.
    """
    uppercase_letters = string.ascii_uppercase  # Contains all uppercase letters.
    lowercase_letters = string.ascii_lowercase  # Contains all lowercase letters.

    if char.isupper():
        # Find the index of the uppercase character in the uppercase alphabet.
        original_index = uppercase_letters.index(char)
        # Calculate the new index after rotation, using the modulo operator (%)
        # to wrap around the alphabet if the rotation goes beyond Z.
        new_index = (original_index + number) % 26
        # Return the uppercase letter at the new index.
        return uppercase_letters[new_index]
    elif char.islower():
        # Find the index of the lowercase character in the lowercase alphabet.
        original_index = lowercase_letters.index(char)
        # Calculate the new index after rotation, wrapping around if necessary.
        new_index = (original_index + number) % 26
        # Return the lowercase letter at the new index.
        return lowercase_letters[new_index]
    else:
        # If the character is not an uppercase or lowercase letter, return it as is.
        return char

def caesar_cipher(text, number):
    """
    Applies the Caesar cipher encryption to a given text.

    Args:
        text (str): The text to be encrypted.
        number (int): The number of positions to shift each letter.

    Returns:
        str: The encrypted text.
    """
    # Iterate through each character in the input text.
    # For each character, apply the rotate_char function if it's an alphabet character.
    # If it's not an alphabet character, keep it unchanged.
    # Finally, join all the processed characters back into a single string.
    return ''.join(rotate_char(char, number) if char.isalpha() else char for char in text)

# Check if the file specified by the 'file' variable exists.
if os.path.isfile(file):
    # If the file exists, open it in read mode ('r').
    with open(file, 'r') as input_file:
        # Read the entire content of the file into the 'input_text' variable.
        input_text = input_file.read()

    # Encrypt the content read from the file using the caesar_cipher function.
    # The rotation value (shift) is set to 2. You can change this number to use a different shift.
    encrypted_text = caesar_cipher(input_text, 2)

    # Print the resulting encrypted text to the console.
    print(encrypted_text)
else:
    # If the file specified by 'file' does not exist, print an error message.
    print(f"Error: The file '{file}' was not found in the current directory.")