import requests
url = 'http://127.0.0.1:8000/upload'
files = [('files', open('sajith.txt', 'rb')), ('files', open('hello.txt', 'rb'))]
resp = requests.post(url=url, files = files) 
print(resp.json())