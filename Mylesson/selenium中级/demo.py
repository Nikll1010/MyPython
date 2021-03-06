class ClassA:
    string = "这是一个字符串"

    def instancefunc(self):
        print("这是一个实例方法")
        print(self)

    @classmethod
    def classfunc(cls):
        print("这是一个类方法")
        print(cls)

    @staticmethod
    def staticfun():
        print("这是一个静态方法")


test = ClassA()  # 初始化一个ClassA对象，test是类ClassA的实例对象
test.instancefunc()  # 对象调用实例方法
test.classfunc()  # 对象调用类方法
test.staticfun()  # 对象调用静态方法

print(test.string)

ClassA.instancefunc(test)  # 类调用实例方法，需要带参数，这里的test是一个对象参数
ClassA.instancefunc(ClassA)  # 类调用实例方法，需要带参数，这里的ClassA是一个类参数
ClassA.staticfun()  # 调用静态方法
ClassA.classfunc()  # 调用类方法
print(ClassA.string)
