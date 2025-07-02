


def pattern1(num):
    for i in range(1,num+1):
        print(' '*(num-i),end='')
        for j in range(i):
            print(i,end=' ')
        print('')

print(pattern1(10))


