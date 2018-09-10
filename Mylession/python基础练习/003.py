def myfun(n):
    if n == 1:
        return 1
    else:
        return n * myfun(n-1)
number = 5
print(myfun(number))
