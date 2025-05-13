# Importing the Required Libraries
import re  # Imports the regular expression module for pattern matching.
import requests  # Imports the requests library for making HTTP requests.
import subprocess  # Imports the subprocess module for running external commands like 'echo' and 'curl'.
import json  # Imports the json module for working with JSON data (though not directly used in this script).

# Regular expression for checking the URL format.
# It checks if the URL starts with 'https://www.', followed by 0 to 25 alphanumeric characters,
# and ends with either '.com' or '.co.uk'.
check_url = r'^https://www\.[a-zA-Z0-9]{0,25}(\.com|\.co.uk)$'

# Defines a URL for the Coinbase API to get the buy price of Bitcoin in British Pounds (GBP).
coinbase = f'https://api.coinbase.com/v2/prices/BTC-GBP/buy'

def separator():
    # Printing a separator line in the terminal.
    # This function uses the 'echo' command via subprocess to print a long line of '====='.
    for i in range(2):
        subprocess.run(["echo", "========================================================================================================================="])


def ssl_request(www_arg):
    """
    Makes an HTTPS request to the provided URL and prints the status code.
    If the status code is 200 (OK), it attempts to make a curl request to the same URL.

    Parameters:
    - www_arg (str): The part of the URL following 'https://', expected to start with 'www.'.
    """
    url = f'https://{www_arg}'  # Constructs the full HTTPS URL.
    if re.match(check_url, url):  # Checks if the constructed URL matches the defined format.
        try:
            ssl_tls_request = requests.get(f'{url}')  # Makes an HTTP GET request to the URL.
            print(ssl_tls_request.status_code)  # Prints the HTTP status code of the response.

            if ssl_tls_request.status_code == 200:  # Checks if the request was successful (status code 200).
                try:
                    # Attempting to make a curl request to the URL.
                    # 'curl' is a command-line tool for transferring data from or to a server.
                    subprocess.run(['curl', f'{url}'])
                except OSError as e:
                    print(e)  # Catches potential OSError exceptions that might occur when running 'curl'.
        except requests.exceptions.RequestException as e:
            print(e)  # Catches potential exceptions that might occur during the 'requests.get()' call.
    else:
        print(f'\'{url}\' doesn\'t match the expected syntax.')
        separator()  # Calls the separator function to print a line.

def check_www(arg):
    """
    Checks if a given URL starts with 'www.' and, if so, prints a message and calls ssl_request.
    
    Parameters:
    - arg (str): The URL to check.
    
    Returns:
    - bool: True if the URL starts with 'www.', False otherwise.
    """
    try:
        if re.match(r'^www\.', arg):  # Checks if the input URL starts with 'www.'.
            print(f'{arg} starts with www')
            ssl_request(arg)  # Calls the ssl_request function to make an HTTPS request.
            return True
        else:
            print(False)
            return False
    except OSError as e:
        print(e)  # Catches potential OSError exceptions that might occur during the regex matching.

# Continuously prompt the user for a URL and check if it starts with 'www.'
while True:
    input_url = input('\n\nEnter a url to request: ')  # Prompts the user to enter a URL.
    check_www(input_url)  # Calls the check_www function to process the entered URL.