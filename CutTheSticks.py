'''
Created on Jan 28, 2017

@author: vbera
'''
n = int(input().strip())
arr = [ int(x) for x in input().strip().split(' ')]
arr = sorted(arr, reverse=True)
lengthArr = len(arr)
while lengthArr > 0:
    print(lengthArr)
    minValue = arr[len(arr) - 1]
    arr[:] = [x - minValue for x in arr]
    zIndex = arr.index(0)
    arr = arr[0:zIndex]
    lengthArr = len(arr)
    
    