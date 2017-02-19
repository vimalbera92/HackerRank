'''
Created on Jan 24, 2017

@author: vbera
'''
import math

n = int(input())

while n > 0:
    a, b = map(int, input().strip().split(' '))
    s = math.sqrt(a)
    e = math.sqrt(b)
    sInt = math.floor(s)
    eInt = math.ceil(e)
    if s == sInt and e == eInt:
        print(eInt - sInt + 1)
    elif s != sInt and e != eInt:
        print(eInt - sInt - 1)
    else:
        print(eInt - sInt)
    n -= 1
