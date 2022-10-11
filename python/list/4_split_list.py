data = open('sketch.txt')
for each_line in data:
    if each_line.find(":") != -1:  # 找不到的情况返回-1
        role, line_spoken = each_line.split(":", 1)  # 这里不加参数1，当遇到多个：的时候就会分成三部分赋值会报错
        print(role, end='')
        print('said', end='')
        print(line_spoken, end='')

data.close('sketch.txt')
