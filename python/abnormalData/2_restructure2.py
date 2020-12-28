import json
def get_stored_username():
    """如果存储了用户名，就获取它"""
    file_name = 'name_file.json'
    try:
        with open(file_name) as file:
            username =json.load(file)
    except:
        return None
    else:
        return  username

def get_new_username():
    #提示用户输入姓名
    username = input("请输入用户名：")
    file_name = 'name_file.json'
    with open(file_name,'a') as file:
        json.dump(username, file)
    return username

def greet_username():
    #问候用户，并指出其名字
    username=get_stored_username()
    if username:
        print("welcome back", username + "!")
    else:
        username=get_new_username()
        print("we'll remember you when you come back", username + "!")

greet_username()