#!/usr/bin/python3

if __name__ == '__main__':
    import requests
    import sys

    response = requests.get(sys.argv[1])
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
