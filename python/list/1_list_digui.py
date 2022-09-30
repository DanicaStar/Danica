'''
列表嵌套列表，怎样打印出列表中的所有元素
1、for层次循环遍历
2、函数递归

'''

str=[1,2,3,12,[99,[2,113,4,]]]
'''
#1
for x in str:
    if isinstance(x,list):
        for y in x:
            print(y)
    else:
        print(x)
'''
#2
def func(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            func(each_item)
        else:
            print(each_item)
func(str)

