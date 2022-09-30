import requests
url='https://xiaoke.kaikeba.com/example/canteen/index.html'
res=requests.get (url)
print(res.text)