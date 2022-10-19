# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 5:50 下午
# @Author  : danica
# @FileName: iter_range.py
# @Software: PyCharm

class IterRange:
    def __init__(self, num):
        self.num = num
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == self.num:
            raise StopIteration
        return self.count


#  利用迭代器来创建一个自定义range
class MyRange:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return IterRange(self.num)


#  利用生成器来创建一个自定义range
class MyRnageGenerator:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        count = 0
        while count < self.num:
            yield count
            count += 1
        else:
            raise StopIteration


if __name__ == '__main__':
    obj1 = MyRange(10)
    for i in obj1:
        print(i)

    obj2 = MyRange(10)
    for i in obj2:
        print(i)
