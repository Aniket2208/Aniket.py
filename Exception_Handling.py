a = 5
b = 0
x = [1,2,3]
z = {'1': "A", '2': "B", '3': "C"}


try:
    print('Start')
    print(z.keys(a))
    y = int(input('Enter thr value '))
    c = a / b
    print(x[3])

except ZeroDivisionError as e:
    print("can't devide by 0")

except IndexError as e:
    print("list index out of range")

except ValueError as e:
    print("invalid literal for int() with base 10")

except Exception as e:
    print(e)

finally:
    print('End')

