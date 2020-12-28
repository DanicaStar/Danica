# #1、列表中存储字典
# aliens=[
#     {'color':'green','points':5},
#     {'color':'red','points':15},
#     {'color':'yellow','points':10},
# ]
# for alien in aliens:
#     print(alien)

# #用一个空列表来存储新增的外星人信息
# aliens=[]
# for alien in range(10):
#     new_alien={'color':'green','points':5}
#     aliens.append(new_alien)
# print(aliens)
# #修改外星人的特人
# for alien in aliens[0:5]:
#     if alien['color']=='green':
#         alien['color']='red'
#         alien['points']=10
#     print(alien)




# #2、字典中存储列表
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
print("你点了一个"+pizza['crust']+"口味的披萨","披萨的配料如下：")
for material in pizza['toppings']:
    print('\t'+material )

#3、字典中存储字典
users={
    'lisa':{
        'first':'albert',
        'last':'lisa',
        'location':'nanjing',
    },
    'alise':{
        'first':'marie',
        'last':'alise',
        'location':'wuhan',
    },
}

for username,infos in users.items():
    full_name=infos['first']+infos['last']
    location=infos['location']
    print('username:'+username)
    print('\tfull_name:'+full_name)
    print("\tlocation:"+location)





