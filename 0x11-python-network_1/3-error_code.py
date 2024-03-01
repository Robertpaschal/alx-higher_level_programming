#!/usr/bin/python3
"""
This script takes in URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
It handles urllib.error.HTTPError exceptions.
"""

import urllib.request
import urllib.error
import sys


def main():
    """
    Sends a request to the specified URL and displays the body
    of the response (decoded in utf-8). Handles HTTPS errors.
    """
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    main()
