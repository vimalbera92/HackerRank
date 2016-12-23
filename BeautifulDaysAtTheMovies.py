'''
Created on Dec 12, 2016

@author: vbera
'''
i,j,k = map(int,input().strip().split(' '))
count = 0
for num in range(i,j):
    rev = int((str(num))[::-1])
    if (rev-num)%k ==0:
        count += 1

print(count)