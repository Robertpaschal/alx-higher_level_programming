#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user ID.
"""

import requests
import sys


def main():
    """
    Retrives the GitHub user ID
    using Basic Authentication with personal access token
    """
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    try:
        response = requests.get(url, auth=(username, password))
        data = response.json()

        if 'id' in data:
            print("User ID:", data['id'])
        else:
            print("Failed to retrive user ID.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
