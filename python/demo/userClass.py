class Name:
    def __init__(self,name):
        self.name=name
class Age(Name):
    def __init__(self,name,age):
        Name.__init__(self,name)
        self.age=age
    def run(self):
        print("我是%s,今年%d岁"%(self.name,self.age))

name=input("请输入姓名")
age=int(input("请输入年龄"))

xiao=Age(name,age)
xiao.run()


        