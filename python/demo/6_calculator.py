def jia(x, y):
    '''相加'''
    return x + y


def jian(x, y):
    '''相减'''
    return x - y


def cheng(x, y):
    '''相乘'''
    return x * y


def chu(x, y):
    '''相除'''
    return x / y


print("选择运算/n1、相加/n2、相减/n3、相乘/n4、相除/n")
choice = int(input("请输入你的选择（1/2/3/4）："))
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))
if choice == 1:
    print("%f+%f=" % (num1, num2), jia(num1, num2))
if choice == 2:
    print("%f+%f=" % (num1, num2), jian(num1, num2))
if choice == 3:
    print("%f+%f=" % (num1, num2), cheng(num1, num2))
if choice == 4:
    print("%f+%f=" % (num1, num2), chu(num1, num2))
