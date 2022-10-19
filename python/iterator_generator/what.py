# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 5:50 下午
# @Author  : danica
# @FileName: what.py
# @Software: PyCharm

# 迭代器、可迭代对象，生成器
# 1、迭代器
"""
1、类中定义了 __iter__ 和 __next__方法
2、__iter__ 方法需要返回对象本身，即：self
3、__next__方法，返回下一个数据，如果没有数据，要抛出StopIteration的异常，可用一个try,except去捕获异常
"""


class iteratior1:
    def __init__(self):
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count < 10:
            return self.count
        else:
            raise StopIteration


## 2、可迭代对象
class Foo:
    def __iter__(self):
        return self  # 返回迭代器对象 / 生成器对象


obj2 = Foo()  # obj是一个可迭代对象
"""
可迭代对象是可以通过for来进行循环
在循环内部其实先执行__iter__方法获得其迭代器对象，然后再内部执行next()，逐步取值
"""
for i in obj2:
    pass

# 3、生成器
"""
使用了 yield 的函数被称为生成器（generator）（生成器是一个边迭代边计算的迭代器）
生成器是一个返回迭代器的函数，只能用于迭代操作，调用一个生成器函数，返回的是一个迭代器对象
"""


# 创建生成器函数
def func():
    yield 1
    yield 2


# 创建生成器对象（内部是根据生成器类generator创建的对象），
# 生成器的内部也声明了 __iter__ 和 __next__方法
obj3 = func()
print(next(obj3))
print(next(obj3))

if __name__ == '__main__':
    obj1 = iteratior1()
    for i in obj1:
        print(i)

from collections.abc import Iterable, Iterator

""" Iterable 可迭代对象，Iterator迭代器"""  # dir(v1),可查看对象的属性和方法
v1 = [11, 222, 33, 44]
print(isinstance(v1, Iterator))  # false，判断是否是迭代器，判断依据是否有__iter__ 和 __next__
print(isinstance(v1, Iterable))  # true，判断是否可迭代，判断依据是否有__iter__且返回迭代器对象
v2 = v1.__iter__()
print(isinstance(v2, Iterator))
print(isinstance(v2, Iterable))
