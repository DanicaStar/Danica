print('''====通讯录管理系统====
1、增加姓名和手机
2、删除姓名
3、修改手机
4、查询所有用户
5、根据姓名查找手机号
6、退出程序''')
tongxunlu={"小王":"123","小张":"345"}
num = int(input("请输入选择项："))
while num < 7:
    if num==1:
        name=input("请输入姓名：")
        pho=input("请输入手机号：")
        tongxunlu[name]=pho
        print("存储成功")
        print(tongxunlu)
    elif num==2:
        name=input("请输入需要删除的姓名：")
        del tongxunlu[name]
        print("删除成功")
        print(tongxunlu)
    elif num==3:
        name=input("请输入被修改手机的姓名：")
        pho=input("请输入手机号号：")
        tongxunlu[name]=pho
        print("修改成功")
        print(tongxunlu)
    elif num==4:
        print(tongxunlu)
        print("查询成功")
    elif num==5:
        name=input("请输入被查找的姓名：")
        print(name+"手机号为"+str(tongxunlu[name]))
        print("查询成功")
    elif num==6:
        print("退出程序")
    num = int(input("请输入选择项："))
else:
    print("end")

