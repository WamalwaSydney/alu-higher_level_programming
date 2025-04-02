#!/usr/bin/python3
"""Send a POST request with a letter parameter and display user info from JSON."""

import requests
import sys

if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    data = {'q': q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json_data = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
