'''
Created on Oct 14, 2016

@author: vbera
'''
import string
i = 0
aToz = list(string.ascii_lowercase)
dic = {x:aToz.index(x) for x in aToz}

no = int(input())
while no > 0:
    line = input()
    ans = ''
    done = False
    i = len(line) - 1
    while i >= 0:
        if not done and line[i] > line[i - 1]:
            ans += line[i - 1] + line[i]
            i -= 2
            done = True
        else:
            ans += line[i]
            i -= 1
    print(ans[::-1])
    no = no - 1
