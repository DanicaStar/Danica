import  requests
url='https://www.zhihu.com/api/v4/members/lisanshui1230/articles'
headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
offset=20
params={
'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
'offset': str(offset),
'limit': '10',
'sort_by': 'created'
}
res=requests.get(url=url,headers=headers,params=params)
res_json=res.json()
# articles=res_json['data']
print(res_json)
# for article in articles:
#     print(article['title'])