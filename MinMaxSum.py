'''
Created on Dec 11, 2016

@author: vbera
'''
import sys

a = map(int, input().strip().split(' '))
minVal = sys.maxsize
maxVal = 0
answer = 0
for t in a:
    answer += t
    if t > maxVal:
        maxVal = t
    if t < minVal:
        minVal = t

print(answer-maxVal, answer-minVal)