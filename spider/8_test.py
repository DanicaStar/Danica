# 题⽬要求：
# 已给出⽹址请⼤家⾃⾏分析⽹站结构，将下图⽤红框圈出来的部分爬取到本地并写⼊excel 表格中,数据取前12条即可。
# 地址: https://www.shobserver.com/news/list?section=42

import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'https://www.shobserver.com/news/list?section=42'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
wb=openpyxl.Workbook()
sheet=wb.active
sheet.titie='Sheet'
list_title=['新闻标题','新闻内容','作者']
sheet.append(list_title)

res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'html.parser')
datas=soup.find_all('div',class_="chengshi")
for data in datas:
    name=data.find('div',class_="chengshi_wz_h").text
    content = data.find('div', class_="chengshi_wz_m").text
    auther = data.find('div', class_="chengshi_wz_f").text
    sheet.append([name,content,auther])
wb.save('test.xlsx')
wb.close()
