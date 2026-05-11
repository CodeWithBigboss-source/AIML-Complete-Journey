# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# data = response.json()

# print(data)

# import requests
# url = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(url)
# data = response.json()
# # print(data)A


# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# payload = {
#     "title": "Hello",
#     "body": "This is a test",
#     "userId": 1
# }

# response = requests.post(url, json=payload)

# print(response.json())


import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    "title": "Hello",
    "body": "This is a test",
    "userId": 1
}
response = requests.put(url,json=data)
print(response.json())