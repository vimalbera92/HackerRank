'''
Created on Feb 19, 2017

@author: vbera
'''
n,m = [int(x) for x in input().split()]
maxi = 0
cnt = 0
inp = [input() for _ in range(n)]
for i in range(0,n-1):
    for j in range(i+1,n):
        set_bit = bin(int(inp[i],2) | (int(inp[j],2))).count("1")
        if set_bit>maxi:
            maxi = set_bit
            cnt = 1
        elif set_bit == maxi:
            cnt+=1
print(maxi)
print(cnt)
     
