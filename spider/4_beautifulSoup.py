# 分析：
# 1、获取菜品名称：p,class="name"
# 2、获取菜品链接：url+a['href']
# 3、获取菜品材料：p,class="ing ellipsis"


# import requests
# from bs4 import BeautifulSoup
# headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# url='http://www.xiachufang.com/explore/'
#
# res=requests.get(url,headers=headers)
# soup=BeautifulSoup(res.text,'html.parser')
# datas=soup.find_all('div',class_="info pure-u")
# for data in datas:
#     name=data.find('p',class_="name").text.replace(' ','').replace('\n','')
#     url_1=url+data.find('a')['href']
#     material=data.find('p',class_="ing ellipsis").text.replace(' ','').replace('\n','')
#     print('菜品名称:{}\n菜品链接：{}\n菜品材料：{}\n'.format(name,material,url_1))


import requests
from bs4 import BeautifulSoup
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
url='https://www.hunanhr.cn/fayangao/2019/0624/464300.html'

res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'html.parser')
datas=soup.find_all('div',class_="zhengwen")
for data in datas:
    names=data.find_all('p')
    for name in names:
        print(name.text)



