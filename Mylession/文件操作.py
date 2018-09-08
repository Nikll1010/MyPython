import os
import io
f = open('boy_1.txt', 'ab')
# b = f.decode('utf-8')
f.read()
# print(b)
print(f)
str = '你好啊,好久不见'
contern = str.encode('utf-8')
f.write(contern)
# a = f.readlines()
# print(a)
