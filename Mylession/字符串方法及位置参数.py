# 字符串内置方法
a = r"abcdabcd    ABCD"
print(a)
b = a.capitalize()  # 把字符串的第一个字符改为大写,其余小写
print(b)
c = a.casefold()  # 把字符串的所有字符改为小写
print(c)
d = a.center(20)  # 把字符串居中，并填充为长度为20的字符串
print(d)
e = a.count('a')  # 计算a在字符串中出现的次数
print(e)
f = a.expandtabs(tabsize=8)  # 把字符串中的\t转化为指定参数，tabsize默认等于8（空格）
print(f)
g = 'x'.join(a)
print(g)
h = "{0} love {1} {2}".format('i', 'fish', '.com')  # 位置参数
print(h)
i = "{a} love {b} {c}".format(a='i', b='fish', c='.com')  # 关键字参数
print(i)
j = "{0} love {1} {c}".format('i', 'fish', c='.com')  # 位置参数和关键字参数混用
print(j)
# k = "{a} love {0} {c}".format(a='i', 'fish', c='.com') 关键字参数必须在位置参数之后，要不然会报错
# print(k)
print("{0}".format('www'))
print('{0}:{1:.2f}'.format('圆周率', 3.1415926))  # 格式化操作符
# 格式化操作符
print('%c' % 97)
print('%5.1f' % 27.111)
print('%.2e' % 27.11111)
print('%10d' % 5)
print('%-10d' % 5)
print('%010d' % 5)
print('%#X' % 100)
print('%#o' % 100)
print(f"{100:d} 的八进制为{1000:o}")
print("%d 的十六进制为%x" % (100, 100))
