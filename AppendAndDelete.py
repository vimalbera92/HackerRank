'''
Created on Dec 20, 2016

@author: vbera
'''

def findSteps(a, b):
    i = 0
    while (i < len(a) and i < len(b)) and a[i] == b[i]:
        i += 1
    
    steps = (len(b) - i) * 2 + (len(a) - len(b))    
    return steps
    
s = input().strip()
t = input().strip()
k = int(input().strip())

answer = 0
if len(s) >= len(t) :
    answer = findSteps(s, t)
else:
    answer = 0

if answer <= k:
    print('YES')
else:
    print('NO')
