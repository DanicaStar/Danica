# # 1、标题  'div',class="ask-list-detials" ('a')
# # 2、网址信息        ('a')['href']
#
# import requests
# from bs4 import BeautifulSoup
# headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# url='https://www.guokr.com/ask/highlight/?page=1'
# res=requests.get(url,headers=headers)
# soup=BeautifulSoup(res.text,'html.parser')
# datas=soup.find_all('div',class_="ask-list-detials")
# for data in datas:
#     name=data.find('h2').text
#     url_1 = data.find('a')['href']
#     print('标题:{}\n新闻链接：{}\n'.format(name,url_1))


import  requests
from  bs4  import  BeautifulSoup
url  =  'https://www.so.com/s'
headers  =  {
        'User-Agent':  'Mozilla/5.0  (Windows  NT  10.0;  Win64;  x64)  AppleWebKit/537.36  (KHTML,  like  Gecko)  Chrome/84.0.4147.125  Safari/537.36  Edg/84.0.522.59'
}

try:
        keyword  =  input('请输入搜索关键字：')
        parameter  =  {
                'q':  keyword
        }
        res  =  requests.get(url=url,headers=headers,params=parameter)
        bs  =  BeautifulSoup(res.text,'html.parser')
        data  =  bs.find('span',class_='nums')
        print(data.text)
except:
        print('爬取失败')