'''
Created on Oct 22, 2016

@author: vbera
'''
import math
length = int(input())
food = input()
sleep = input()

pairs = []
for i in range(length):
    pairs.append((food[i], sleep[i]))

N = int(input())
while N > 0:
    answer = 0
    L, R = map(int, input().strip().split(' '))
    count = sorted(sleep[L - 1:R]).count('0')
    if count > 0:
        answer = math.factorial(count - 1)
    
    new_food = pairs[L - 1:R]
    new_food.sort(key=lambda pair: pair[1])
    first = new_food[0:count]
    second = new_food[count:len(new_food)]
    
    if len(second) > 0:
        for i in range(len(first)):
            match = 0
            for j in range(len(second)):
                if first[i][0] == second[j][0]:
                    match += 1
            answer += math.factorial(match)

    if len(new_food) - count > 0:
        answer += math.factorial(len(new_food) - count - 1)


    if len(first) > 0:
        for i in range(len(second)):
            match = 0
            for j in range(len(first)):
                if second[i][0] == first[j][0]:
                    match += 1
            answer += math.factorial(match)
    
    print(answer)
    N -= 1
