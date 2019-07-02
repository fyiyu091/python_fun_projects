import requests

r = requests.get("https://www.google.com/")
print(r.url)
print(r.headers)
print(r.encoding)
print(r.cookies)