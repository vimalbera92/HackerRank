'''
Created on Dec 12, 2016

@author: vbera
'''
n = int(input().strip())
while n>0:
    no, sweets, starts = map(int,input().strip().split())
    temp = sweets + starts - 1
    prisoner = temp % no
    if prisoner == 0:
        print(no)
    else:
        print(prisoner)    
    n -= 1