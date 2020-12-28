'''
利用多协程和队列，来爬取豆瓣图书Top250（书名，作者，评分）并存储csv
豆瓣图书：https://book.douban.com/top250?start=0
1、获取数据
2、解析数据
3、提取数据
4、存储数据
'''
import  requests
from bs4 import BeautifulSoup
import csv
def douban_book_spider():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    url = 'https://book.douban.com/top250'
    for i in range(3):
        params = {
            'start': str(i * 25)
        }
        reponse = requests.get(url=url, headers=headers, params=params)
        soup = BeautifulSoup(reponse.text, 'html.parser')
        datas = soup.find_all('tr', class_="item")
        for data in datas:
            book_name = data.find('div', class_="pl2").text.replace('\n', '').replace(' ', '')
            auther = data.find('p', class_="pl").text
            rating = data.find('span', class_="rating_nums").text
            # print(book_name,rating,auther)
            with open('douban_book.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([book_name, rating, auther])

douban_book_spider()

