#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.qo/status
and displays the body of the response
"""

import requests


def main():
    """
    Fetches the URL https://alx-intranet.hbtn.io/status
    and displays the body of the response
    """


url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
except requests.exceptions.RequestException as e:
    print("Error fetching the URL:", e)


if __name__ == "__main__":
    main()
