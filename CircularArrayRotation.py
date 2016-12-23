'''
Created on Nov 14, 2016

@author: vbera
'''

n,k,q = map(int,input().strip().split(' '))
a = [int(a_temp) for a_temp in input().strip().split(' ')]
for a0 in range(q):
    m = int(input().strip())
    print(a[(m-k)%n])
    
