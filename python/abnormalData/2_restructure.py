import json
def get_stored_username():
    file_name= 'name_file.json'
    try:
        with open(file_name) as file:
            username=json.load(file)
    except:
        return None
    else:
        return username

def greet_username():
    file_name = 'name_file.json'
    username=get_stored_username()
    if username:
        print("welcome back", username + "!")
    else:
        username=input("请输入姓名：")
        with open(file_name,'a+') as file:
            json.dump(username,file)
            print("we'll remember you when you come back", username + "!")

greet_username()