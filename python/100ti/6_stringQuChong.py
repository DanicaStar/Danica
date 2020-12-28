# s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
list=[]
for i in s:
    if i not in list:
        list.append(i)
list.sort()
res=','.join(list)
print(res)