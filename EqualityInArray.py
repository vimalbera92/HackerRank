'''
Created on Jan 28, 2017

@author: vbera
'''
import operator

nTotal = int(input())
numbers = input().strip().split(' ')
nDict = {}
for n in numbers:
    count = nDict.get(n)
    if count == None:
        count = 0
    nDict[n] = count + 1
sorted_nDict = sorted(nDict.items(), key=operator.itemgetter(1), reverse=True)
print(nTotal-sorted_nDict[0][1])
