'''
Created on Dec 11, 2016

@author: vbera
'''

h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()
height,width=0,0
for c in word:
    width += 1
    if height < h[ord(c)-ord('a')]:
        height = h[ord(c)-ord('a')]

print(height * width)