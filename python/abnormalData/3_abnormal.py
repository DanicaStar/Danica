# #ZeroDivisionError: division by zero
# print("请输入两个数，将运算出两个数的商")
# print("输入'q'退出")
# while True:
#     first_num=input('第一个数：')
#     if first_num=='q':
#         break
#     second_num = input('第二个数：')
#     if second_num=='q':
#         break
#     try:
#         answer=int(first_num)/int(second_num)
#     except ZeroDivisionError:
#         print("第二个数不能为0")
#     else:
#         print(answer)


#FileNotFoundError
try:
    file_name="programming123.txt"
    with open(file_name) as file:
        lines=file.readlines()
        print(lines)
except FileNotFoundError:
    print("sorry,the ",file_name," does not exist")