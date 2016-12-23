'''
Created on Oct 13, 2016

@author: vbera
'''
n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
i = 0
jump = 0
while i < n - 1:
    if i + 2 < n and c[i + 2] != 1:
        i = i + 2
    else:
        i = i + 1
    jump += 1
    
print(jump)
