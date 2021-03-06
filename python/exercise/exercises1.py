#1、一行代码实现1--100之和
# print(sum(range(1,101)))

#2、如何在一个函数内部修改全局变量
#函数内部global声明 修改全局变量

#3、列出5个python标准库
# os：提供了不少与操作系统相关联的函数
# sys: 通常用于命令行参数
# re: 正则匹配
# math: 数学运算
# datetime:处理日期时间

#4、字典如何删除键和合并两个字典
# dic1={'a':1,'b':2,'c':3,'d':4,'e':5,}
# dic2={'f':6,'g':7,'h':8}
# dic3=dic1
# del dic3['a']    #删除字典
# dic2.update(dic1)   #合并字典
# print(dic3)
# print(dic2)


# #5、python实现列表去重的方法
# lst=[1,3,45,6,7,3,2,3,6]
# b=set(lst)
# print(b)


# #列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
# lst=[1,2,3,4,5]
# def fn(x):
#     return x**2
# res=map(fn,lst)
# res=[i for i in res if i>10]
# print(res)

#python中生成随机整数、随机小数、0--1之间小数方法
# import random
# # 1、随机整数：random.randint(a,b),生成区间内的整数
# print(random.randint(2,9))
# # 2、随机小数：习惯用numpy库，利用np.random.randn(5)生成5个随机小数
# import numpy as np
# print(np.random.randn(5))
# # 3、0-1随机小数：random.random(),括号中不传参
# print(random.random())
# # 4、随机一个大于0小于9的小数
# print(random.uniform(0,9)) #随机一个大于0小于9的小数
# #验证码生成器
# import random
# def code():
#     code = ''
#     for i in range(4):
#         ran1=random.randint(0,9)
#         ran2=chr(random.randint(60,95))
#         add=random.choice([ran1,ran2])
#         code=''.join([code,str(add)])
#     return code
# print(code())

# # s = "ajldjlajfdljfddd" 去重并从小到大排序输出"adfjl"
# s="ajldjlajfdljfddd"
# s=set(s)       #set()是临时去重，想要永久去重可以赋值给新变量
# lst=list(s)
# lst.sort(reverse=False)
# str=''.join(lst)
# print(str)

# #用lambda函数实现两个数相乘
# product=lambda a,b:a*b
# print(product(2,4))

# # 24、字典根据键从小到大排序
# dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
# lst=sorted(dic.items(),key=lambda i:i[0],reverse=False)
# print(dict(lst))
#

# #"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# s="kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# dic={}
# for i in s:
#     if i in dic:
#         dic[i] +=1
#     else:
#         dic[i]=1
# print(dic)
# #本题的解法2：
# from collections import Counter
# res=Counter(s)
# print(res)

# #27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def fn(a):
#     return a%2==1
# lst=filter(fn,a)
# lst=[i for i in lst]
# print(lst)

# #28、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([i for i in a if i%2==1 ])

# #33、请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
# import time,datetime
# print(time.strftime('%Y-%m-%d %H:%M:%S')+" 星期"+str(datetime.datetime.now().isoweekday()))


#36、写一段自定义异常代码,自定义异常用raise抛出异常


# # 39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
# a=[[1,2],[3,4],[5,6]]
# lst=[j for i in a for j in i]
# print(lst)


# # 40、x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
# x="abc"
# y="def"
# z=["d","e","f"]
# print(x.join(y))
# print(x.join(z))

# # 43、举例说明zip（）函数用法
# # # 可以接受任何类型的序列，同时也可以有两个以上的参数;当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组
# # a=[1,2]
# # b=[3,4]
# # print([i for i in zip(a,b)])
# # c=(1,2)
# # d=(3,4)
# # print([i for i in zip(c,d)])
# # e='ab'
# # f='xyz'
# # print([i for i in zip(f,e)])
# A=zip(('a','b','c','d','e'),(1,2,3,4,5))
# A0=dict(A)
# A1=range(10)
# A2=[i for i in A1 if i in A0]
# A3=[A0[s] for s in A0]
# print('A0',A0)
# print(A2)
# print(A3)




# # 52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
# # 利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，递归调用获取最小值的函数，反复操作
# list=[2,3,5,4,9,6]
# lst=[]
# def get_min(list):
#     a=min(list)
#     list.remove(a)
#     lst.append(a)
#     if len(list)>0:
#         get_min(list)
#     return lst
# lst=get_min(list)
# print(lst)



# # 53、写一个单列模式
# # 因为创建对象时__new__方法执行，并且必须return 返回实例化出来的对象所cls.__instance是否存在，不存在的话就创建对象，存在的话就返回该对象，来保证只有一个实例对象存在（单列），打印ID，值一样，说明对象同一个
# class Singleton():
#     __instance=None
#
#     def __new__(cls, age,name):
#         #如果属性__instance的值为None
#         #那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时能够知道之前已经创建过对象了
#         if not cls.__instance:
#             cls.__instance=object.__new__(cls)
#         return cls.__instance
# a=Singleton(18,'alise')
# b=Singleton(6,'json')
# print(id(a))
# print(id(b))
# a.age=22 #给a指向的对象的age属性
# print(b.age)


# # 54、保留两位小数
# a="%.03f"%1.3335
# print(a,type(a))
# print(round(float(a), 1))
# print(round(float(a), 2))


# 61、简述同源策略,同源策略需要同时满足以下三点要求：
#  1）协议相同
#  2）域名相同
#  3）端口相同
# http:www.test.com与https:www.test.com 不同源——协议不同
# http:www.test.com与http:www.admin.com 不同源——域名不同
# http: www.test.com与http:www.test.com: 8081 不同源——端口不同

# 62、简述cookie和session的区别
# 1，session 在服务器端，cookie 在客户端（浏览器）
# 2、session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，如果浏览器禁用了 cookie ，同时 session 也会失效，存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置
# 3、cookie安全性比session差

# # 66、python中copy和deepcopy区别
# import copy
# list=[1,2,[3,4]]
# a=copy.copy(list)
# b=copy.deepcopy(list)
# list[0]=10
# list[2][0]=9
# print(a)
# print(b)

# 71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
# list=[0,-1,3,-10,5,9]
# list.sort(reverse=False)       #sort()是在list的基础上进行修改，无返回值
# res=sorted(list,reverse=False) #sorted()有返回值
# print(list)
# print(res)

# # 72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# res1=sorted(foo,key=lambda x:x)
# res2=sorted(foo,key=lambda x:(x<0,abs(x)))  #正数从小到大，负数从大到小
# print(res1)
# print(res2)
#
# # 74、列表嵌套字典的排序，分别根据年龄和姓名排序
# foo = [{"name":"zs","age":19},{"name":"ll","age":54},
#         {"name":"wa","age":17},{"name":"df","age":23}]
# res1=sorted(foo,key=lambda x:x['age'],reverse=True)
# res2=sorted(foo,key=lambda x:x['name'])
# print(res1)
# print(res2)

# # 75、列表嵌套元组，分别按字母和数字排序
# foo = [('zs',19),('ll',54),('wa',17),('df',23)]
# res1=sorted(foo,key=lambda x:x[1],reverse=True)
# res2=sorted(foo,key=lambda x:x[0])
# print(res1)
# print(res2)

# # 75、列表嵌套列表，分别按字母和数字排序
# # foo = [['zs',19],['ll',54],['wa',23],['df',19]]
# # res1=sorted(foo,key=lambda x:x[1],reverse=True)
# # res2=sorted(foo,key=lambda x:(x[1],x[0]))
# # print(res1)
# # print(res2)

# # 80、最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用
# s=['ab','abc','a','wxyz']
# b=sorted(s,key=lambda x:len(x))
# print(b)

# # 举例说明SQL注入和解决办法
# input_name='danica;drop database demo'
# sql='select * from demo where name="%s" ' % input_name
# print("SQL注入语句",sql)   #执行的时候会删除数据库demo
# # 解决方式：通过传参数方式解决SQL注入
# params=[input_name]
# count=excute('select * from demo where name=%s',params)












