'''
Created on Dec 11, 2016

@author: vbera
'''

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

kangaroo1 = False
kangaroo2 = False

if x1==x2:
    print("YES")
else:
    if v1 > v2:
        kangaroo1 = True
    else:
        kangaroo2 = True
    
    if kangaroo1:
        while x1 < x2:
            x1 += v1
            x2 += v2
    else:
        while x2 < x1:
            x1 += v1
            x2 += v2
    if x1==x2:
        print("YES")
    else:
        print("NO")    