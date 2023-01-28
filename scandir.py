# Import the requests library to enable web requests to be processed.
import requests
from termcolor import colored

# Create variables for the URL to target and the wordlist for directory names.
target_url = input('[+] What is the target URL (exclude http://)? ')
file_name = input('[+] Enter the directory wordlist: ')

# Create a function for processing requests and returning the page responses if connection is successful.
def request(url):
    try:
        # First, return the request from the given URL...
        return requests.get("http://" + url)
        # Except if the response is a connection error, then just pass.
    except requests.exceptions.ConnectionError:
        pass

# Open the wordlist file for 'r' (reading).
file = open(file_name, 'r')
# For each line in the wordlist, run the following script (until the whole file has been run)
for line in file:
    # Set the directory name from the file to variable 'directory', and strip any extra characters from the string in the file.
    directory = line.strip()
    # Set the 'full_url' variable to the entire URL - the target, plus the directory.
    full_url = target_url + '/' + directory
    # Store the response in  the 'response' variable (which will be null if the response is a connection error)
    response = request(full_url)
    # If the 'response' variable contains data, then print the following message.
    if response:
        print('[+] Directory discovered: ' + full_url)