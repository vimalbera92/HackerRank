'''
Created on Nov 9, 2016

@author: vbera
'''
n = int(input())
binN = "{0:b}".format(n)
num = 0
count = 0
prev = False
for i in binN:
    if i == '1':
        if prev == False:
            prev = True
        count += 1
    else:
        if num < count:
            num = count
        count = 0    
        prev = False
if num < count:
    num = count

print(num)
