#
# #<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
#
# import re
# str='<dav class="name">中国</div>'
# res=re.findall(r'<dav class=".*">(.*?)</div>',str)
# '''
# . 表示可有可无
# * 代表任意字符
# '''
# print(res)


import re

a = 'xxIxxjshdxxlovexxsffaxxpythonxx'

infos = re.findall('xx(.*?)xx',a)

print(infos)