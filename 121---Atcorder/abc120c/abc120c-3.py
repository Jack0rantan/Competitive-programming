import sys
import os

# input file
f = open('testinput_c.txt', 'r')
sys.stdin = f

a = ["0","1"]
S = input()
print(2*min(map(S.count, a)))
