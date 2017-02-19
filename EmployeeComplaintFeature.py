'''
Created on Feb 6, 2017

@author: vbera
'''

def getPath(emp,tree):
    path = []
    parent = emp
    while parent != 1:
        parent = tree[parent]
        path.append(parent)
    return path
    
totalEmp = int(input().strip())
justiceFactors = [int(t) for t in input().strip().split(' ')]
hierarchyOfEmp = {}
hierarchy = input().strip().split(' ')
for i in range(2, totalEmp + 1):
    hierarchyOfEmp[i] = int(hierarchy[i - 2])

testcases = int(input().strip())
while testcases > 0:
    emp1, emp2 = map(int, input().strip().split(' '))
    pathOfEmp1 = getPath(emp1, hierarchyOfEmp)
    pathOfEmp2 = getPath(emp2, hierarchyOfEmp)
    justiceIndex = 1
    i = len(pathOfEmp1) - 1
    j = len(pathOfEmp2) - 1
    while i >=0 and j >=0 and pathOfEmp1[i] == pathOfEmp2[j]:
        if justiceFactors[justiceIndex] < justiceFactors[pathOfEmp1[i]]:
            justiceIndex = pathOfEmp1[i]
        i -= 1
        j -= 1
    print(justiceIndex)
    testcases -= 1