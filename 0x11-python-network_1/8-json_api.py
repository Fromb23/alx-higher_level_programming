#!/usr/bin/python3
"""
    Search API
"""

if __name__ == '__main__':
    import requests
    import sys

    letter = ""
    if len(sys.argv) < 2:
        q = ""
    else:
        letter = sys.argv[1]

    data = {'q': letter}

    url = "https://0.0.0.0:5000/search_user"
    response = requests.post(url, data=data)

    response_json = response.json()

    try:
        if response_json:
            print(f"{response_json['id']} {response_json['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
