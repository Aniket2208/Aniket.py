class A():

    def __init__(self,m,h,e):
        self.m=m
        self.h=h
        self.e=e

    def dis(self):
        print('class A')

    def add(self,x='null',y='null',z='null'):
        if(x!='null' and y!='null' and z!='null'):
            return x+y+z
        elif(x!='null' and y!='null'):
            return x+y
        else:
            return x

class B(A):

    def dis(self):
        print('class B')

a=B(1,1,1)

print(a.dis())
