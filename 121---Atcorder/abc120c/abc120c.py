import sys
import os

# input file
f = open('testinput_c.txt', 'r')
sys.stdin = f

e = []
ans = 0
S = list(input())

for k in S:
    e.append(k)
    if(len(e)>1):
        if(e[-1] != e[-2]):
            ans += 2
            e.pop()
            e.pop()
print(ans)
