info={"aa":"a123","bb":"b123","dd":"d123","cc":"c123"}  #存储系统账户名、密码
while True:
    answer= int(input("======登入系统======\n1、登录\n2、注册\n3、修改\n4、退出\n请输入想要运行的功能序号："))
    #answer==1,进入登录界面
    if answer==1:   
        #输入用户名
        user=input("请输入用户名：")
        #判断用户名为空，要提示重新输入
        if len(user)==0:
            user=input("用户名不能为空，请重新输入：")  
        #判断用户名不为空
        if len(user) !=0:
            #用户名已存在
            if user in info:
                    #请输入密码
                    while True:
                        pwd=input("请输入密码：")
                        #密码为空，提示要重新输入
                        if len(pwd)==0:
                            user=input("密码不能为空，请重新输入：")   
                        if len(pwd) !=0:
                            #密码正确，提示登录成功
                            if pwd == info[user]:
                                print("登录系统成功")
                                #登录成功，就跳出循环，回到首页
                                break  
                            else:
                                print("密码错误，1、重新输入2、忘记密码")
                                answer1=int(input("请输入1或者2:"))
                                if answer1==1:
                                    continue
                                else:
                                    word=input("修改密码，请输入q回到首页选择修改功能:")
                                    break           
            #判断用户名不存在
            else:
                print("该用户不存在")     
                word=input("请输入q回到首页选择注册功能:")   
                #回到首页  
                continue                                                                          
    #answer==2,进入注册界面
    elif answer==2:
        #输入用户名
        user=input("请输入用户名：")
        #判断用户名为空，要提示重新输入
        if len(user)==0:
            user=input("用户名不能为空，请重新输入：") 
        #判断用户名不为空       
        elif len(user)!=0:
            #判断用户名已存在
            if user in info:
                print("%s用户已存在"%(user))
                word=input("请输入q回到首页选择登录功能:")  
                    
            #判断用户名不存在
            else:
                pwd=input("请输入密码：") 
                #密码为空，提示要重新输入
                if len(pwd)==0:
                    pwd=input("密码不能为空，请重新输入：")
                #判断密码不能低于8位
                elif len(pwd) !=0:
                    while len(pwd)<8:
                        pwd=input("密码不能低于8位,请重新输入:")
                    #判断密码长度超过8位，注册成功
                    else:
                        info[user]=pwd
                        print("%s注册成功,密码为%s"%(user,pwd))
                        #跳出循环，回到首页
                        break  
    #answer==2,进入修改界面
    elif answer==3:
        user=input("请输入要修改的用户名：")
        pwd=input("请输入密码：")
        while len(pwd)<8: 
            pwd=input("密码不能低于8位,请重新输入:")
        #判断密码长度超过8位，注册成功
        else:
            info[user]=pwd
            print("%s密码修改成功,密码为%s"%(user,pwd))
            #跳出循环，回到首页
            break  
    #answer==2,进入退出界面
    elif answer==4:
        print("欢迎下次使用")
        #结束整个进程
        break                                             
    else:
        pass
	
	     
		

