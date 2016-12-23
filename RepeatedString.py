'''
Created on Oct 13, 2016

@author: vbera
'''
s = input().strip()
n = int(input().strip())

count = s.count('a')
div = int(n / len(s))
reminder = n % len(s)
ans = div * count + (s[:reminder].count('a'))
print(ans)
