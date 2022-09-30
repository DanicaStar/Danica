
# 需要两个接口，都需要参数，歌曲的eferer有变化，歌词的mid有变化，都需要构造
# # 歌词url对应的参数
# lyric_params={
#     'nobase64': 1,
#     'musicid': 447810,
#     '-': 'jsonp1',
#     'g_tk_new_20200303': 1349113291,
#     'g_tk': 1563071098,
#     'loginUin': 420155623,
#     'hostUin': 0,
#     'format': 'json',
#     'inCharset': 'utf8',
#     'outCharset': 'utf-8',
#     'notice': 0,
#     'platform': 'yqq.json',
#     'needNewCode': 0
# }
# lyric_url='https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'        #通过分析，musicid不同
# # url1='https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg?nobase64=1&musicid=107709592&-=jsonp1&g_tk_new_20200303=1349113291&g_tk=1563071098&loginUin=420155623&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
# # url2='https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg?nobase64=1&musicid=447810&-=jsonp1&g_tk_new_20200303=1349113291&g_   tk=1563071098&loginUin=420155623&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
# lyric_headers={
#     'user-agent':' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
#     'origin':' https://y.qq.com',
#     'referer':''      #通过分析，不同的部分对应的是歌曲的mid
#     # 'referer':' https://y.qq.com/n/yqq/song/003g4dpV4bOEJs.html'  #你不是真正的快乐
#     # 'referer':' https://y.qq.com/n/yqq/song/0022QuVR1LcRHN.html'  后来的我们
# }




import  requests
choice=input("请输入歌手名称：")
for i in range(1,4):   #构造动态获取页码
    song_url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'  #通过对比，P对应的值不同
    # url1='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=70472416157537416&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E4%BA%94%E6%9C%88%E5%A4%A9&g_tk_new_20200303=1349113291&g_tk=1563071098&loginUin=420155623&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    # url2='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=70472416157537416&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=2&n=10&w=%E4%BA%94%E6%9C%88%E5%A4%A9&g_tk_new_20200303=1349113291&g_tk=1563071098&loginUin=420155623&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    song_headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'origin':'https://y.qq.com',
        'referer':'https://y.qq.com/portal/search.html'
    }
    # 歌曲url对应的参数
    song_params={
        'ct': '24',
        'qqmusic_ver':' 1298',
        'new_json': 1,
        'remoteplace': 'txt.yqq.song',
        'searchid': '68360851316746497',
        't': '0',
        'aggr': '1',
        'cr':' 1',
        'catZhida':' 1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(i),     #页面
        'n': '10',
        'w': choice,
        'g_tk_new_20200303': '1349113291',
        'g_tk': '1563071098',
        'loginUin': '420155623',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform':' yqq.json',
        'needNewCode':'0'
    }
    res = requests.get(url=song_url, headers=song_headers, params=song_params)
    try:
        if res.status_code==200:
            res_json=res.json()
            song_list = res_json['data']['song']['list']
            for song in song_list:
                name = song['name']
                mid = song['mid']
                id = song['id']
                #歌词url对应的参数
                lyric_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
                lyric_headers = {
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                    'origin': 'https://y.qq.com',
                    'referer':'https://y.qq.com/n/yqq/song/{}.html'.format(mid)   # 通过分析，不同的部分对应的是歌曲的mid
                }

                lyric_params = {
                    'nobase64': 1,
                    'musicid': str(id),
                    '-': 'jsonp1',
                    'g_tk_new_20200303': 1349113291,
                    'g_tk': 1563071098,
                    'loginUin': 420155623,
                    'hostUin': 0,
                    'format': 'json',
                    'inCharset': 'utf8',
                    'outCharset': 'utf-8',
                    'notice': 0,
                    'platform': 'yqq.json',
                    'needNewCode': 0
                }
                lyric_res = requests.get(url=lyric_url, headers=lyric_headers, params=lyric_params)
                json_lyric_res = lyric_res.json()
                lyric = json_lyric_res['lyric']
                print(name,lyric)
                print(' ')
        else:
            print("请求失败")
    except Exception as error:
        print(error)







#
