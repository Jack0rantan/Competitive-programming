import sys
import os

# input file
f = open('testinput.txt', 'r')
sys.stdin = f

def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = set(table)
    return table

# file read
a, b, c = map(int, input().split())

elm = sorted(list(divisor(a) & divisor(b)), reverse = True)
print(elm[c-1])
