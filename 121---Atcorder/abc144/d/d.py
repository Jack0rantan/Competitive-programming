input = open('input.txt','r').readline

import math
a,b,x=map(int,input().split())
l = a**2*b
rx = l-x
rl = rx / a**2
if 2*rl <= b:
    print(math.degrees(math.atan(2*rl/a)))
else:
    print(math.degrees(math.atan(b**2*a/(x*2))))