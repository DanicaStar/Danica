import random
# # 1、生成随机整数
# print(random.randint(1,5))
#
# # 2、生成随机小数
# print(random.random())   #随机大于0 且小于1 之间的小数
#
# #3、随机一个大于0小于9的小数
# print(random.uniform(0,9)) #随机一个大于0小于9的小数

# def random_num():
#     code = ''
#     for i in range(4):
#         ran1 = random.randint(0,9)
#         ran2 = chr(random.randint(65,90))
#         add = random.choice([ran1,ran2])
#         code = ''.join([code,str(add)])
#     return code
#
# rand_n = random_num()
# print(rand_n)



#验证码生成器
def num():
    code=''
    for i in range(4):
        ran1=random.randint(0,9)
        ran2=chr(random.randint(65,90))
        add=random.choice([ran1,ran2])
        code=''.join([code,str(add)])
    return code
num=num()
print(num)