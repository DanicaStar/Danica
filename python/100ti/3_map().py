# list1=[1,2,3,4,5]
# def fn(x):
#     return x**2
# res=map(fn,list1)
'''
map()是 python 内置的高阶函数,它接收一个函数 f 和一个 list
并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的object并返回
'''
# res=[i for i in res if i >10]
# print(res)

list1=[1,2,3,4,5]
list2=[]
for i in list1:
    i=i**2
    if i>10:
        list2.append(i)
print(list2)