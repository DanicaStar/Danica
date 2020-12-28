import json
file_name= 'name_file.json'
try:
    with open(file_name) as file:
        username = json.load(file)
except:
    username = input("请输入用户名：")
    with open(file_name, 'a+') as file:
        json.dump(username, file)
        print("we'll remember you when you come back", username + "!")
else:
    print("welcome back", username + "!")



