# f.write('laalal')
# f.readline().join((1,1,1))
# print(f)
# f
# print(f.read(5))
# print(f.tell())
# f.seek(0,0)
f = open(r'D:\BaiduNetdiskDownload\Python\record.txt')
boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:3] != '===':
        (role, line_spoken) = each_line.split(':', 1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    else:
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        # boy = []
        # girl = []
        count += 1
f.close()
