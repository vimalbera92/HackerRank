'''
Created on Feb 20, 2017

@author: vbera
'''
t = int(input().strip())

while t > 0:
    b, w = map(int, input().strip().split(" "))
    x, y, z = map(int, input().strip().split(" "))
    bCost = 0
    wCost = 0
    if x > y + z:
        bCost = (y + z) * b
    else:
        bCost = b * x
    if y > x + z:
        wCost = (x + z) * w
    else:
        wCost = w * y
    print(bCost + wCost)
    t -= 1
