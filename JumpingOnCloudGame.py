'''
Created on Dec 12, 2016

@author: vbera
'''

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

current = k
if current >= n:
    current = current % n
energy = 100
if c[0] == 1:
    energy -= 2
energy -= 1 
while current != 0:
    if c[current] == 1:
        energy -= 3
    else:
        energy -= 1
    current += k
    if current >= n:
        current = current % n

print(energy) 