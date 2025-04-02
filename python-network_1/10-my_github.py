#!/usr/bin/python3
"""Fetch GitHub user id using Basic Authentication."""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get("https://api.github.com/user", auth=(username, password))
    try:
        json_data = response.json()
    except ValueError:
        print("None")
    else:
        print(json_data.get("id"))
