'''
Created on Nov 15, 2016

@author: vbera
'''
input_str = input()
temp = input_str[0]
minVal = 0
sec_index = 0
cut = []
for i in range(1, len(input_str)):
    for j in range(sec_index + 1, len(input_str)):
        temp = temp + input_str[j]
        if temp == temp[::-1]:
            minVal = j
    temp = ''
    if minVal != -1:
        cut.append(minVal)
        sec_index = minVal
        minVal = -1 
print(cut)
