import requests  # Imports the 'requests' library, which is used for making HTTP requests.

# Sends an HTTP GET request to the specified URL.
# 'https://jsonplaceholder.typicode.com/posts' is a free online REST API for testing.
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Iterates through the headers of the HTTP response.
for i in response.headers:
    # Prints each header name from the response. Headers contain metadata about the response.
    print(i)

# Prints the HTTP status code of the response.
# Common status codes include 200 (OK), 404 (Not Found), 500 (Internal Server Error), etc.
print(response.status_code)
