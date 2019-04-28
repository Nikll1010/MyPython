TEP = input("请输入华氏度，以F结尾")
# c = input("请输入华氏度，以C结尾")
if TEP[-1] in ['F', 'f']:
    C = (eval(TEP[0: -1]) - 32) / 18
    print("转换后的温度是{:.2f}C".format(C))
elif TEP[-1] in ['C', 'c']:
    F = 1.8 * eval(TEP[0: -1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("格式输入错误")
