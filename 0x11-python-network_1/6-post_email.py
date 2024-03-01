#!/usr/bin/python3
"""
This script takes in a URL na d an email address, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response.
"""

import requests
import sys


def main():
    """
    Sends a POST request to the specified URL with the email as a parameter
    and displays the body of the response.
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'Your email is': email}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error fetching the URL:", e)


if __name__ == "__main__":
    main()
