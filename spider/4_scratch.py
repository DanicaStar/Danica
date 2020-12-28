import requests
from bs4 import BeautifulSoup
url = 'https://xiaoke.kaikeba.com/example/canteen/index.html'
res = requests.get (url)
print(res.status_code)
soup = BeautifulSoup(res.text,'html.parser')
items = soup.find_all(class_='show-list-item') #使用find()方法提取首个<div>元素，并放到变量item里。
print(type(items)) #打印item的数据类型
for item in items:
    title=item.find(class_="desc-title").text
    material = item.find(class_="desc-material").text
    step = item.find(class_="desc-step").text
    print(title,material,step)  # 打印itemxa0

