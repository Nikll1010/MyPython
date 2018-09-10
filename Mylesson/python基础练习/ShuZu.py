man = [1, 'asas', [1, 2, 3], "www"]
print(man)
man.append([1, 2, 3])
ma = [1, 2, '111']
man.append(ma)  # append（）方法是把一个元素添加为man的一个元素
print(man)
man.extend(ma)  # extend()方法添加的是列表数组中的元素一个一个添加进去
print(man)
man.insert(1, ma)  # 把ma添加到man列表的第一个元素位置，注意：列表的元素开始是从0开始的
print(man)
name = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
print(name)
name[1], name[3] = name[3], name[1]  # 元素互换
print(name)
# name[3] = name[1]
# print(name)
name.remove('zhangsan')#指定删除已知的元素名称
name.remove('lis')#删除不存在元素会报错
del name[1]#删除指定位置的元素