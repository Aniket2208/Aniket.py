
position = -1
l = [1,2,3,4,5]
n = 5

def search(l,n):

    for i in range(len(l)):
        if l[i]==n:
            globals()['position'] = i
            return True

    return False


if search(l,n):
    print('Found at position', position+1)
else:
    print('Not found')