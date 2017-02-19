s = int(input())
n = int(input())
inputNumbers = {}
while n > 0:
    temp = int(input())
    inputNumbers[temp] = 0
    n -= 1

for key in inputNumbers.keys():
    b = s - key
    if inputNumbers.get(b) != None:
        print(1)
        exit(0) 
