def hansi(n,x,y,z):
    if n == 1:
        print(x +'-->'+ z)
    else:
        hansi(n-1,x,z,y)#把a上n-1个盘子借助z移到y上
        print(x +'-->'+ z)#把a上最后一个把盘子移到z上
        hansi(n-1,y,x,z)#再把b上的n-1个盘子借助x移到z上
hansi(4,'X','Y','Z')