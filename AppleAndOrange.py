'''
Created on Dec 11, 2016

@author: vbera
'''
s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

appleCount, orangeCount = 0,0
for ap in apple:
    if ap+a >= s and ap+a <=t:
        appleCount += 1
        
for ora in orange:
    if ora+b >=s and ora+b <= t:
        orangeCount += 1

print(appleCount)
print(orangeCount)