class A():

    def __init__(self):
        print('init A')

    def display1(self):
        print('Class A')

class B():

    def __init__(self):
        super().__init__()
        print('init B')

    def display2(self):
        print('Class B')

class D():

    def __init__(self):
        super().__init__()
        print('init D')

    def disD(self):
        print('Class D')

class E():

    def __init__(self):
        super().__init__()
        print('init E')

    def disE(self):
        print('Class E')

class C(D,E,A,B):

    def __init__(self):
        print('init C')
        super().__init__()

    def dis3(self):
        print('Class C')

a = A()
b = B()
c = C()
# c = C()
#
# a.display1()
# b.display1()
# b.display2()
# c.display1()
# c.display2()
# c.dis3()
# c.disD()

