#!/usr/bin/python3
"""
This script fetch https://alx-intranet.hbtn.io/status
and displays information about the response
"""

import urllib.request


def main():
    """
    Fetches the URL https://alx-intranet.hbtn.io/status
    and displays information abou the response
    """

    url = "https://alx-intranet.hbtn.io/status"

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            utf8_content = body.decode('utf-8')
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
            print("\t- utf8 content:", utf8_content)
    except urllib.error.URLError as e:
        print("Error fetching the URL:", e)


if __name__ == "__main__":
    main()
