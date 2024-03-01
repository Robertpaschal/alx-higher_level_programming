#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the body of the response. If the HTTP status
code is greater than or equal to 400, it prints an error code.
"""

import requests
import sys


def main():
    """
    Sends a request to the specified URL and displays the body
    of the response. Prints an error code if the HTTP status ccode
    is greater than or equal to 400.
    """
    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error fetching the URL:", e)


if __name__ == "__main__":
    main()
