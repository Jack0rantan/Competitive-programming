import sys
import os

# input file
f = open('testinput.txt', 'r')
sys.stdin = f

import fractions
a , b , k= map(int, input().split())


li = []
for i in range(1, 101):
    if a % i == 0 and b % i == 0:
        li.append(i)

print(li[-k])
