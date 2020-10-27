import requests

# response = requests.get('https://xkcd.com/353/')
# response_2 = requests.get('https://xkcd.com/353/jvkgjvdfkdfj/')

# print(dir(response))

# print(help(response))
# print(F"the status code of request is {response.status_code}")
# print(response_2.status_code)

# print(F"the URL of the request is {response.url}")

# print(F"this is the text attribute: \n\n{response.text}")
# print(F"this is the text attribute: \n\n{response.content}")

# response = requests.get("https://imgs.xkcd.com/comics/python.png")

# print(response.content)
# print(response.text)

# with open("new2_photo.png", 'wb') as file:
# 	file.write(response.content)

parameters = {"name": "python", "school": "basic IT"}

response = requests.get('https://httpbin.org/get', params = parameters)

# response = requests.get('https://httpbin.org/get?name=python&school=basic+IT')
# print(response.url)
print(response.text)

r = response.json()
print(type(r))
print(r['args'])
print(r['args']["name"])
