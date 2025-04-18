#!/usr/bin/python3
"""Fetch and display the X-Request-Id header from a URL using urllib."""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.getheader("X-Request-Id")
    print(header)
