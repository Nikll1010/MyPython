while True:

    year = int(input('请输入年份：'))

    a = year % 4 == 0

    b = year % 100 != 0

    c = year % 400 == 0

    is_lip = a and b or c
    if not is_lip:
        print("不是闰年")
    else:
        print("是闰年")
