'''
Created on Oct 18, 2016

@author: vbera
'''
def  maxElement(arr):
    maxVal = -1
    arr.sort(reverse=True)
    for i in range(len(arr)-2):
        ele = arr[i]
        for j in range(i,len(arr)-2):
            k = arr.index(ele-arr[j+1])  if arr.count(ele-arr[j+1]) >= 1 else -1
            if k != -1 and k > j+1:
                return arr[i]
    return maxVal        
        
ans = maxElement([1,2,3,6])
print(ans)