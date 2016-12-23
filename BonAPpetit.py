'''
Created on Dec 12, 2016

@author: vbera
'''
n,k = map(int,input().strip().split(' '))
cost = [int(a_temp) for a_temp in input().strip().split(' ')]
charge = int(input())

totalShare = 0
for iCost in cost:
    totalShare += iCost
    
totalShare = (totalShare - cost[k])/2
if totalShare == charge:
    print('Bon Appetit')
else:
    print(int(charge-totalShare))
