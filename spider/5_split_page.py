import  requests
for i in range(1,4):
    # url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='+str(i*20)
    url = 'https://movie.douban.com/j/search_subjects'
    headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    params={
        'type': 'movie',
        'tag': '热门',
        'sort': 'recommend',
        'page_limit': '20',
        'page_start': str(i*20)
    }
    res=requests.get(url,headers=headers,params=params)
    res_json=res.json()
    movie_list=res_json["subjects"]
    # print(movie_list)
    for movie in movie_list:
        name=movie['title']
        print(name)