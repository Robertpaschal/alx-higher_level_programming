#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the X-Request-id variable found
in the header of thr response.
"""

import urllib.request
import sys


def main():
    """
    Sends a request to the specified URL and displays the value
    of the X-Request-Id variable found in the response header.
    """
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as repsonse:
            request_id = repsonse.getheader('X-Request-Id')
            if request_id:
                print(request_id)
    except urllib.error.URLError as e:
        print("Erro fetching the URL:", e)


if __name__ == "__main__":
    main()
