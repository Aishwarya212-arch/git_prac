


def pattern1(num):
    for i in range(1,num+1):
        print(' '*(num-i),end='')
        for j in range(i):
            print(i,end=' ')
        print('')

print(pattern1(10))


def pattern2(final_letter):
    alphabet={chr(i):i-64 for i in range(65,91)}
    seen=[]
    for k in alphabet.keys():
        if k==final_letter:
         seen.append(k)
         break
        else:
           seen.append(k)
    for j in range(len(seen)):
       print(' '*(len(seen)-j), end='')
       if j==0:
          print(seen[0],end='  ')
       else:
          for l in range(j+1):
             if l==j:
                print(seen[j])
             print(seen[l],end='  ')
      