import requests

r = requests.get("https://www.oneplus.com/7pro#/")
print(r.url)
print(r.headers)
print(r.encoding)
print('----------------')
print(r._content)