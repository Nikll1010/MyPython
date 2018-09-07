

for i in range(0, len("i love you")):
    # a = "i love you"[i]
    # print('第' + str(i) + '个字符为' + a)
    a = 'i love you'[i]
    print('第{0}个字符为{1}'.format(i+1, a))
for each in "i love you":
    print(each)
n = 0
for x in "i love you":
    n = n + 1
    print("第{0}个字符为{1}".format(n, x))
