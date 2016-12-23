'''
Created on Nov 3, 2016

@author: vbera
'''
import re
def recurssion(no):
    ans = 0
    if no == 0:
        return 1
    elif no >= 3:
        ans = ans + recurssion(no - 3)
        ans = ans + recurssion(no - 2)
        ans = ans + recurssion(no - 1)
    elif no >= 2:    
        ans = ans + recurssion(no - 2)
        ans = ans + recurssion(no - 1)
    elif no >= 1:
        ans = ans + recurssion(no - 1)
    return ans

s = int(input().strip())
n = []
for a0 in range(s):
    n = int(input().strip())
    ans = recurssion(n)
    print(ans)


asd = re.compile("asdf")
asd.