import  requests
url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=58764958097143811&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E4%BA%94%E6%9C%88%E5%A4%A9&g_tk_new_20200303=1349113291&g_tk=1563071098&loginUin=420155623&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
res=requests.get(url)
res_json=res.json()
# print(res_json)
list_music = res_json['data']['song']['list']
for music in list_music:
    print('歌名：' + music['name'])

    # 以name为键，查找歌曲名

    print('所属专辑：' + music['album']['name'])

    # 查找专辑名

    print('播放时长：' + str(music['interval']) + '秒')
    print(' ')
