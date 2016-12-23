'''
Created on Oct 26, 2016

@author: vbera
'''

#!/bin/python3


time = input().strip()
hours = int(time.split(':')[0])
if time[-2:] == 'PM':
    if hours < 11:
        hours += 12
else:
    if hours == 12:
        hours = '00'
ans = str(hours,)+time[2:-2]
print(ans)