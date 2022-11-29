class A:

    def __init__(self):
        self.name = "Ani"
        self.age = 22

    def update(self):
        self.age = 30

    def compare(self, other):
        if (a.age == b.age):
            return True
        else:
            return False

a = A()
b = A()
b.name = 'Danny'
b.update()

if a.compare(b):
    print("Same age")
else:
    print("Different age")


print(a.name, a.age)
print(b.name, b.age)
