#!/usr/bin/python3
"""
    A script that takes url and email, sends a POST
    requst to the url with the email passed as args
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    URL = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode('ascii')

    req = urllib.request.Request(URL, data)

    with urllib.request.urlopen(req) as request:
        body = request.read().decode('utf-8')
        print("Your email is: " + body)
