#!/usr/bin/python3
"""
    Error Code
"""

if __name__ == '__main__':
    import requests
    import sys

    response = requests.get(sys.argv[1])
    if reponse.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
