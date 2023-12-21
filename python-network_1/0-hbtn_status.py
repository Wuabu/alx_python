# #!/usr/bin/python3
# import requests

# if __name__ == "__main__":
#     url = "https://alu-intranet.hbtn.io/status"
#     response = requests.get(url)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         print(response.text)
#     else:
#         print(f"Failed to retrieve content. Status code: {response.status_code}")
import requests

if __name__ == '__main__':
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)