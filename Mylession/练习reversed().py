a = [1, 2, 3, 4, 5, 6]
reversed(a)
print(a)
for each in a:
    print(each, end=',')  # end=''表示以''结尾，默认以换行符结尾
for i in reversed(a):
    print(i, end=',')
b = reversed(a)
print(b)