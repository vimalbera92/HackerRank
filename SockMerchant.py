'''
Created on Oct 12, 2016

@author: vbera
'''
n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
c.sort()
answer = 0
i = 0
while i < len(c):
    count = c.count(c[i])
    answer += int(count/2)
    i += count
print(answer)
    