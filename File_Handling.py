
f = open('Data', 'r')

# print(f.readline(), end='')
# print(f.readline(), end="")
# print(f.readline(4), end='')

f1 = open('abc', 'w')
# print(f1.write("in Pycharm"))

# f1 = open("abc", "a")
# print(f1.write(" writting a file"))

# for data in f:
#    f1.write(data)

f2 = open('Healthcare.jpg', 'rb')

f3 = open('A.jpg', 'wb')

for i in f2:
   f3.write(i)
