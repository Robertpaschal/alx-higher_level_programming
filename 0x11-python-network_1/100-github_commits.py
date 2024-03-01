#!/usr/bin/python3
"""
This script retieves 10 most recent commits of a repository
using the GitHub API
"""

import requests
import sys


def main():
    """
    Retrieves 10 most recent commits of a repository
     using the GitHub API
    """
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = (
        f"https://api.github.com/repos/{owner_name}/"
        f"{repository_name}/commits"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            for commit in data[:10]:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print("Error:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
