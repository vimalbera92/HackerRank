'''
Created on Dec 20, 2016

@author: vbera
'''
import sys

def findMinSteps(a, b):
    i = 0
    while (i < len(a) and i < len(b)) and a[i] == b[i]:
        i += 1
    
    steps = (len(b) - i) * 2 + (len(a) - len(b))    
    return steps
    
s = input().strip()
t = input().strip()
k = int(input().strip())

minSteps = findMinSteps(s, t)
if minSteps == 0 and k >= len(t) * 2:
    print('Yes')
elif k == minSteps:
    print('Yes')
elif k > minSteps:
    if k - minSteps % 2 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')