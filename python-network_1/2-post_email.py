#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Data to be sent in the POST request
    data = {'email': email}

    # Send POST request
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)
