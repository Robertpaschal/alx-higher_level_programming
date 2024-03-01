#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys


def main():
    """
    Sends a POST request to the specifed URL with the email as a parameter
    and displays the body of the response (decoded in utf-8).
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    try:
        with urllib.request.urlopen(url, data=data) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print("Error fetching the URL:", e)


if __name__ == "__main__":
    main()
