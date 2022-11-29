class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is", self.cpu, self.ram)

a = Computer('i5','16')
b = Computer('Ryzon3','8')
#print(type(a))

#Computer.config(a)

a.config()
b.config()