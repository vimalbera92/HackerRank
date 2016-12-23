'''
Created on Oct 22, 2016

@author: vbera
'''
N = int(input())
while N > 0:
    comb = set()
    inputString = input();
    length = len(inputString)
    for i in range(length):
        s = inputString[i:length]+inputString[0:i]
        if comb.__contains__(s):
            break;
        comb.add(s)
    print(len(comb))
    N -= 1