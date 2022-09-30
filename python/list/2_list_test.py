'''
the_list=[1,210,3,12,[99,[2,113,4,],142],124]
找出列表中的最大值好最小值
'''



'''
解题思路
加入list=[1,0,4,2,3]

max:1 1 4 4 4
min:1 0 0 0 0

max        min
1 vs 0
1 vs 4
4 vs 2   0 vs 2
4 vs 3   0 vs 3

'''
the_list = [1, 210, 3, 12, [99,-5,[2, 113,0, 4, ], 142], 124,495]
the_list1=[]
def func(the_list):   #首先获取到列表中的值，每个都打印出来，获得一个新的列表
    for each_item in the_list:
        if isinstance(each_item,list):
            func(each_item)
        else:
            # print(each_item)
            the_list1.append(each_item)
    return the_list1


def max_min():
    para=func(the_list)
    max_value = para[0]
    min_value = para[0]
    for j in para[1:]:
        if j>max_value:
            max_value=j
        if j<min_value:
            min_value=j
    print(max_value,min_value)

if __name__ == '__main__':
    max_min()
