# #ZeroDivisionError: division by zero
# print("请输入两个数，将运算出两个数的和")
# print("输入'q'退出")
# while True:
#     first_num=input('第一个数：')
#     if first_num=='q':
#         break
#     second_num = input('第二个数：')
#     if second_num=='q':
#         break
#     try:
#         answer=int(first_num)+int(second_num)
#     except :
#         print("输入的内容必须为数字")
#     else:
#         print(answer)


def count_words(file_name):
    try:
        with open(file_name) as file:
            contents=file.read()
    except:
        print('文件'+file_name+'不存在')
    else:
        words=contents.split()
        num_words = len(words)
        print('文件{}有{}个单词:'.format(file_name, num_words),end='')
        for word in words:
            print(word,end=',')
        print()
file_names=['programming1.txt','programming2.txt','programming3.txt']
for file_name in file_names:
    count_words(file_name)