#查询所有单车
#进行单车租借
#归还单车
#出租自己的共享单车

class Bick:
    #初始化方法 no代表车辆编号、age代表车辆年限
    #status代表车辆状态  0表示待租借，1表示租借中
    def __init__(self,no,age,state=0):
        self.no=no
        self.age=age
        self.state=state

    def __str__(self):
        if self.state==0:
            status="待租借"
        else:
            status="租借中"
        return '车辆编号%d 已经运行%d年，车辆状态：%s' %(self.no,self.age,status)


class Manage:
    #定义一个列表，用来存储所有的车辆
    bike_list = []

    def __init__(self):
        bickA=Bick(1001,1)
        bickB=Bick(1002,2)
        bickC=Bick(1003,3)
        self.bike_list.append(bickA)
        self.bike_list.append(bickB)
        self.bike_list.append(bickC)
    #菜单系统
    def menu(self):
        print("欢迎进入租车系统")
        while True:
            print('1.查询所有车辆\n2.共享车辆\n3.租借车辆\n4.归还车辆\n5.退出系统\n')
            select = int(input('请输入所选功能对应得数字：'))
            if select==1:
                self.info_bike()
            elif select==2:
                self.add_bike()
            elif select==3:
                self.jie_bike()
            elif select==4:
                self.huan_bike()
            elif select==5:
                print('期待您下次使用！祝您生活愉快！')
                break
    def info_bike(self):
        for bike in self.bike_list:
            print(bike)
    def add_bike(self):
        new_no=int(input("请输入单车的编号："))
        new_age=int(input("请输入车辆使用年限："))

        new_bick=Bick(new_no,new_age)
        self.bike_list.append(new_bick)
        print("车辆共享成功")
    def jie_bike(self):
        jie_no=int(input("请输入单车的编号："))
        res=self.select_bick(jie_no)
        if res != None:
            if res.state==1:
                print("你来晚了，车被租走了")
            else:
                print("租借成功，欢迎您使用绿色出行")
                res.state=1

    def select_bick(self,no):
        for bike in self.bike_list:
            if bike.no==no:
                return bike
            else:
                print("该车辆不存在")
                break
      
    def huan_bike(self):
        huan_no=int(input("请输入单车的编号："))
        res=self.select_bick(huan_no)
        if res != None:
            if res.state ==1:
                print("还车成功，期待下次使用")
                res.atate=0
            else:
                print("车辆等待租借")
        else:
            print("该车辆不存在,想必您是输错了")


user=Manage()
print(user)
user.menu()
