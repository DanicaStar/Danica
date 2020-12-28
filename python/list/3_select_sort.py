# -*- coding:utf-8 -*-
# @Time : 2020-11-01 15:35
# @Author: Danica
# @File : 3_select_sort.py
'''
选择排序
'''

def find_minimal_index(seq):
    min_elem=seq[0]
    count=0
    min_elem_index=count
    for elem in seq[1:]:
        count +=1
        if elem<min_elem:
            elem , min_elem=min_elem , elem
            min_elem_index = count
            print(count)
    return min_elem_index

def select_sort(seq_list):
    seq=seq_list[:]
    length=len(seq)
    for i in range(length):
        index=find_minimal_index(seq[i:])
        seq[index+i] , seq[i]=seq[i],seq[index+i]
        print(seq)
    # return seq
seq=[7,5,6,9,2]
# random.shuffle(seq)
print(select_sort(seq))

