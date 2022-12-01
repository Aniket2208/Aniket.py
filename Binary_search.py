position = -1

l = [1,2,3,4,5,6,7,8,9,10]
n = 10

def search(l,n):
    ll = 0
    ul = len(l)-1

    while ll < ul :
        mid = ll + ul // 2
        if l[mid] == n:
         globals()['position'] = mid
         return True

        else:
            if l[mid] < n:
                ll = mid
            else:
                ul = mid
        ll += 1


    return False


if search(l,n):
    print('Found at position', position+1)
else:
    print('Not found')