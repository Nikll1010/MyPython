a = list()  # 创建一个空列表，输出他的类型
print(type(a))
b = list((1, 2, 3, 4, 5, 6, 7, 8))  # list()方法用于将可迭代对象--元组--生成一个列表
print(b)
c = list("i love you")  # 将可迭代对象--字符串--生成一个列表（注意空格）
print(c)
# tuple()与str() 方法一样，都是将可迭代对象iterable生成相应的对象
d = tuple()
print(type(d))
e = tuple("i love you")
print(e)
f = tuple([1, 2, 3, 4, 5, 6, 7])
print(f)
j = 'i', ' ', 'l', 'o', 'v', 'e'
print(j)
print(len(j))
'''------------'''
g = str()
print(type(g))
h = str([1, 2, 3, 4, 5, 6])
print(h)
print(type(h))
i = str(('i', ' ', 'l', 'o', 'v', 'e', ' ', 'y', 'o', 'u'))
print(i)
