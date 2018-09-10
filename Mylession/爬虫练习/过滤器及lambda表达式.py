# lambda 表达式
g = lambda x: 2 * x + 1
g(5)
print(g(5))

f = lambda x, y: x + y

print(f(1, 2))

# 过滤器filter()
g = filter(None, [0, 1, True, False])  # 返回一个可迭代对象,将任何非True的内容过滤掉
print(g)
g = list(g)  # 将可迭代对象list
print(g)


def add(x):  # 定义filter过滤器
    return x % 2


temp = range(10)

g = filter(add, temp)
g = list(g)
print(g)
# filter 与lambda结合
g = filter(lambda x: x % 2, range(10))

g = list(g)
print(g)

# map()映射
g = list(map(lambda x: x * 2, range(10)))

print(g)
# g = dict(map(lambda x: x * 2, range(10)))

print(g)
