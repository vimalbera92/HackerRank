'''
Created on Dec 12, 2016

@author: vbera
'''
n = int(input().strip())
start = 5
count = 0
while n > 0:
    liked = int(start/2)
    count += liked
    start = liked * 3
    n-=1
print(count)