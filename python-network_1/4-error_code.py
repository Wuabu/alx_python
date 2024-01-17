#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send GET request
    response = requests.get(url)

    # Display the body of the response
    print(response.text)

    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)
