import json
# # name=input("请输入姓名：")
# name=[1,2,3,4,5]
# file_name='name_file.json'
# with open(file_name,'w') as file:
#     json.dump(name,file)


file_name= 'name_file.json'
with open(file_name) as file:
    name=json.load(file)
    print(name)

