#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    # Check if the header is present in the response
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
