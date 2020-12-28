# 1、获取数据
# 2、解析数据
# 3、提取数据
# 4、存取数据   歌曲名称、歌曲专辑、歌曲播放链接
#     1、实例化一个工作簿
#     2、创建？激活一个工作表
#     3、获取工作簿的活动表
#     4、将工作表重命名





import  openpyxl
import  requests
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title ="qq_music"
column_name=['歌曲名','所属专辑','播放链接']
sheet.append(column_name)




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
                album=song['album']['name']
                music_link='https://y.qq.com/n/yqq/{}.html'.format(song['mid'])
                sheet.append([name,album,music_link])
            wb.save('qq_music.xlsx')
            wb.close()
        else:
            print("请求失败")
    except Exception as error:
        print(error)



