import xlrd
#找到xlsx文件
book =xlrd.open_workbook('test.xls')
#读取文件的表
sheet=book.sheets()[0]
#获取表的最大行
rows=sheet.nrows
#获取表的最大列
cols=sheet.ncols
list=[]
key=sheet.row_values(0)
#逐行读取数据
for x in range(1,rows):
    value=(sheet.row_values(x))
    #将每行的数据打包成一个字典
    temp = dict(zip(key, value))
    #将每行的数据以字典的形式添加到列表中
    print(temp)
    # list.append(temp)
# print(list)





