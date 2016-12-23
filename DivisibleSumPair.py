'''
Created on Dec 12, 2016

@author: vbera
'''

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
count = 0
for i in range(n-1):
    for j in range(i+1,n):
        if (a[i]+a[j]) % k == 0:
            count += 1
            
print(count)
