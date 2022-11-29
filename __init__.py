class Computer:

    def __init__(self):
        print("in __init__")

    def config(self):
        print("i5,8Gb,16Tb")

a = Computer()
b = Computer()
#print(type(a))

#Computer.config(a)

a.config()
b.config()