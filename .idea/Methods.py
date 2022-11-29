class Class:

    school = 'SHB'

    def __init__(self,m,h,e):
        self.m = m
        self.h = h
        self.e = e

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def class_name():
        print('This is class 10')

    def avg(self):
        print( (self.m + self.h + self.e)/3)

    def get(self):
        return (self.m, self.h, self.e)

    def set(self,x,y,z):
        self.m = x
        self.h = y
        self.e = z


a = Class(70,60,50)
b = Class(40,50,30)

a.avg()
b.avg()
print(Class.info())
Class.class_name()

# print(a.avg())
# print(b.avg())






