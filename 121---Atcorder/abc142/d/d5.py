input = open('input.txt','r').readline
from math import gcd

g = gcd(*map(int, input().split()))

f = 2
d = {}
while f**2 <= g:
    if g % f:
        f += 1
    else:
        d[f] = d.get(f,0) + 1
        g//=f

if g>1:
    d[g] =d.get(g,0) + 1

print(len(d)+1)