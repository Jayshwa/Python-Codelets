def num_to_binary(n):
    """
    Converts an integer to its 8-bit binary representation.
    This function provides a fundamental view of numerical representation
    in a binary format, a key concept in computer architecture.
    """
    return format(int(n), '08b')

def num_to_hex(n):
    """
    Converts an integer to its hexadecimal representation.
    Hexadecimal serves as a more concise human-readable alternative
    to binary, often employed in representing lower-level data.
    """
    return hex(int(n))

while True:
    user_input = input("Enter a character or number: ")

    # Determine if the input is a numerical value.
    if user_input.isdigit():
        binary_code = num_to_binary(user_input)
        hex_code = num_to_hex(user_input)
    else:
        # For character inputs, the ordinal value is obtained prior to conversion.
        # This illustrates the numerical basis of textual data encoding.
        binary_code = ''.join(format(ord(char), '08b') for char in user_input)
        hex_code = ' '.join(hex(ord(char)) for char in user_input)

    print(f'Binary: {binary_code}')  # Displays the binary equivalent of the input.
    print(f'Hexadecimal: {hex_code}')  # Displays the hexadecimal equivalent of the input.