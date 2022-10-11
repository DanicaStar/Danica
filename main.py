# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 9:37 上午
# @Author  : danica
# @FileName: main.py
# @Software: PyCharm

the_list = [1, 210, 3, 12, 99, -5, 2, 113, 0, 4, 142, 124, 495]


def quick(the_list):
    if len(the_list) < 2:
        return the_list
    else:
        base = the_list[0]
        left = [item for item in the_list[1:] if base > item]
        # left = [elem for elem in the_list[1:] if elem < base]
        right = [item for item in the_list[1:] if base < item]
        # right = [elem for elem in the_list[1:] if elem > base]
        return quick(left) + [base] + quick(right)


print(quick(the_list))

# if __name__ == '__main__':
#     pass
