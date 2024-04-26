#!/usr/bin/python3
"""
    A script that fetches a request
"""

if __name__ == '__main__':
    import requests

    url = "https://alx-intranet.hbtn.io/status"

    r = requests.get(url)
    text = r.text
    print("Body response:")
    print("-\t type:", type(text))
    print("-\t content:", text)
