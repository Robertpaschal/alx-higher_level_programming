#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable found
in the header of the response.
"""

import requests
import sys


def main():
    """
    Sends a request to the specified URL and dsiplays the value
    of the X-Request-Id variable found in the response header.
    """
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(request_id)
    except requests.exceptions.RequestException as e:
        print("Error fetching the URL:", e)


if __name__ == "__main__":
    main()
