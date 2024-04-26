#!/usr/bin/python3

"""Fetches the body of a URL using urllib."""

if __name__ == '__main__':
    import urllib.request

    URL = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(URL) as response:
        read = response.read()
        string_bytes = read.decode('utf-8')
        print("- Body response: ")
        print("\t- type: ", type(read))
        print("\t- content:", read)
        print("\t- utf8 content:", string_bytes)
