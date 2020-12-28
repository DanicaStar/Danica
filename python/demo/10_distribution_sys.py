import math
def func1():
    type = int(input("请选择计算的类型：1--配送次数计算，2--快递员数量计算"))
    size = float(input("请输入项目大小：1代表标准，还可以输入其他倍数或小数"))
    if type==1:
        others= int(input("快递员的数量（请输入整数）为："))
    else:
        others= int(input("配送次数（请输入整数）为："))
    return type,size,others   #这里返回一个数组

def func2(data_input):
    type = data_input[0]
    size = data_input[1]
    others = data_input[2]
    if type == 1:
        num= math.ceil(round(size*100/20/others))
        print("%f.1标准大小的集装箱，%d个快递员，需要配送%d次"%(size,others,num))
    elif type == 2:
        person= math.ceil(round(size*100/20/others))
        print("%f.1标准大小的集装箱，配送%d次，需要%d个快递员"%(size,others,person))
    
def func():
    data_input = func1()
    func2(data_input)

func()