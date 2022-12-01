
l = [5,1,2,3,4]

# for i in range(len(l)-1,0,-1):
#     for j in range(i):
#         if l[j] > l[j+1]:
#             t = l[j]
#             l[j]=l[j+1]
#             l[j+1]=t
# print(l)

def sort(l):

    for i in range(len(l)-1):
        min = i

        for j in range(i,len(l)):
            if l[j] < l[min]:
                min = j

        t = l[i]
        l[i]=l[min]
        l[min]=t

        print(l)

sort(l)
print(l)



