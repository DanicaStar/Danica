'''
利用多协程和队列，来爬取豆瓣图书Top250（书名，作者，评分）并存储csv
豆瓣图书：https://bookdouban.com/top250?start=0
1、获取数据
2、解析数据
3、提取数据
4、存储数据
'''

# 从gevent库中导入monkey模块
from gevent import monkey
from gevent.queue import Queue
# 使用monkey.patch_all()  能够把程序变成协作式运行，帮程序实现异步
from gevent import monkey
monkey.patch_all()
import  requests,csv,gevent
from bs4 import BeautifulSoup
from gevent.queue import Queue


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
work=Queue()   #创建队列对象，并且赋值给work
for i in range(3):
    page=i*25
    url='https://book.douban.com/top250?start='+str(page)
    work.put_nowait(url)   #将请求的url都放入队列中

def douban_book_spider():
    while not work.empty():   #队列为空就不执行下面的任务
        start_url=work.get_nowait()   #get_nowait()  将队列中的url都取出来
        reponse = requests.get(url=start_url, headers=headers)
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
task_list=[]
for i in range(3):
    task = gevent.spawn(douban_book_spider)  # 使用gevent.spawn()创建协程任务
    task_list.append(task)    #将三个任务添加到任务列表
gevent.joinall(task_list)    #gevent.joinall()执行任务列表中的所有任务
