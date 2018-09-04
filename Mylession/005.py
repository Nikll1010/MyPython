class A:
    def __init__(self, size=10):
        self.size = size
        # return self.size

    def getsize(self):
        return self.size

    def setsize(self, value):
        self.size = value

    def delsize(self):
        del self.size
    x = property(getsize, setsize, delsize)
temp = A(10)
temp = int(input('请输入:\n'))
# print(temp.x)
