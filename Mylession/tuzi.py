def mytuzi(n):
    n1 = 1
    n2 = 1
    n3 = 0
    while (n - 2 > 0):
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
        # print(n3)
    return n3


def mytuzi1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return mytuzi1(n - 1) + mytuzi1(n - 2)


print(mytuzi1(20))
