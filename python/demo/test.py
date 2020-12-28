def make_great(first,last,**infos):
    users={}
    users['first'] = first
    users['last'] = last
    for i,j in infos.items():
        users[i]=j
    return users

user=make_great('lisa','danica',location='anhui',field='physics')
print(user)










# def print_name(unprint_name,printed_name):
#     #将unprint_name表中打印完成的数据移到printed_name
#     while unprint_name:
#         current=unprint_name.pop()
#         #打印姓名的过程
#         print('printing_name:'+current)
#         printed_name.append(current)
# def show_name(printed_name):
#     print("\n已经打印完成的姓名如下：")
#     #现实打印的姓名
#     for i in printed_name:
#         print('printed_name：'+i)
#
# unprint_name=['lisa','danica','alise','lily']
# printed_name=[]
# print_name(unprint_name,printed_name)
# show_name(printed_name)




