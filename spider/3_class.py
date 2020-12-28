import  requests
from bs4 import  BeautifulSoup
url='https://www.shicimingju.com/book/sanguoyanyi.html'
response=requests.get(url)
state=response.status_code
print(state)
res=response.text
# print(res)
soup=BeautifulSoup(res,'html.parser')
contents=soup.find_all(class_="book-mulu")
title=contents[0].find_all('li')
for content in title:
    print(content.text)
