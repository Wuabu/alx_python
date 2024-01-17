#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}

    # Send POST request
    response = requests.post(url, data=data)

    try:
        # Parse JSON response
        user_info = response.json()

        # Check if the JSON is not empty
        if user_info:
            print("[{}] {}".format(user_info['id'], user_info['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
