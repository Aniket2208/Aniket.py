class Computer:

    def config(self):
        print("i5,8Gb,16Tb")

a = Computer()
#print(type(a))

Computer.config(a)

print(a.config())

b = 5
print(b.bit_length())
