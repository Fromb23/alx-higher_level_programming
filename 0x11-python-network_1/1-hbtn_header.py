#!/usr/bin/python3
"""
    Sends a request to a URL and displays the value
    of the X-Request-Id var found in the response header
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    URL = sys.argv[1]

    with urllib.request.urlopen(URL) as request:
        header = request.getheader("X-Request-Id", None)
        print(header)
