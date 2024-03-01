#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


def main():
    """
    Sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter. Displays the response accordingly.
    """
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        response = requests.post(url, data={'q': letter})
        data = response.json()

        if data:
            if isinstance(data, dict):
                print("[{}] {}".format(data['id'], data['name']))
            elif isinstance(data, list):
                for item in data:
                    print("[{}] {}".format(item['id'], item['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
