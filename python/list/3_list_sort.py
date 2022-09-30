# a=1
# b=4
# # a,b=b,a+b
# c=0
# c=a
# a=b
# b=c+b
# print(b,a)

the_list = [1, 210, 3, 12, [99, -5, [2, 113, 0, 4, ], 142], 124, 495]
the_list1 = []
class list_sort():
    def get_list(self,the_list):  # 首先获取到列表中的值，每个都打印出来，获得一个新的列表
        for each_item in the_list:
            if isinstance(each_item, list):
                self.get_list(each_item)
            else:
                # print(each_item)
                the_list1.append(each_item)
        return the_list1

    # 1、快速排序
    '''
    对于一串序列，首先从中选取一个数，凡是小于这个数的值就被放在左边一摞，凡是大于这个数的值就被放在右边一摞。
    然后，继续对左右两摞进行快速排序
    '''
    def quick_sort(self,the_list1):
        if len(the_list1) < 2:
            return the_list1
        else:
            base=the_list1[0]
            left=[elem for elem in the_list1[1:]if elem<base]
            # print("left:"+str(left))
            right=[elem for elem in the_list1[1:]if elem>base]
            # print("right:"+str(right))
            # print('return'+str(self.quickSort(left) + [base] + self.quickSort(right)))
            return self.quick_sort(left) + [base] + self.quick_sort(right)


    #2、冒泡排序
    '''
    从左向右，两两比较，如果左边元素大于右边，就交换两个元素的位置
    每一轮排序，序列中最大的元素浮动到最右面。也就是说，每一轮排序，至少确保有一个元素在正确的位置
    '''
    def bouble_sort(self,the_list):
        length=len(the_list1)-1
        for i in range(length):
            for j in range(0,length-1):
                if the_list1[j]>the_list1[j+1]:
                    the_list1[j],the_list1[j + 1]=the_list1[j+1],the_list1[j]
        return the_list1

    #3、选择排序

if __name__ == '__main__':
    sort=list_sort()
    the_list1 = sort.get_list(the_list)
    print(sort.quick_sort(the_list1))
    print(sort.bouble_sort(the_list1))




