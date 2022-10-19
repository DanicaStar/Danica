# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 9:37 上午
# @Author  : danica
# @FileName: main.py
# @Software: PyCharm

lst = [1, 210, 3, 12, 99, -5, 2, 113, 0, 4, 142, 124, 495, 5]


def quick(the_list):
    if len(the_list) < 2:
        return the_list
    else:
        base = the_list[0]
        left = [elem for elem in the_list[1:] if elem < base]
        right = [elem for elem in the_list[1:] if elem > base]
        return quick(left) + [base] + quick(right)


def bouble(the_list):
    length = len(the_list) - 1
    for x in range(length):
        for y in range(length):
            if the_list[y] > the_list[y + 1]:
                the_list[y], the_list[y + 1] = the_list[y + 1], the_list[y]
    return the_list


print(quick(lst))

# if __name__ == '__main__':
#     pass
