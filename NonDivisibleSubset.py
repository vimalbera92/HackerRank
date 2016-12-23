'''
Created on Oct 13, 2016

@author: vbera
'''
n, k = map(int, input().split(' '))
arr = list(map(int, input().strip().split(" ")))

dic = {x:[] for x in range(k)}

for i in range(n): 
    dic[arr[i] % k].append(arr[i])

count = 0

if len(dic[0]) > 0:
    count += 1 

s = set([(x, k - x) for x in range(1, k // 2 + 1)])

for i, j in s:
    if i != j:
        if len(dic[i]) > len(dic[j]):
            count += len(dic[i])
        else:
            count += len(dic[j])
    else:
        if len(dic[i]) > 0:
            count += 1

print(count)
