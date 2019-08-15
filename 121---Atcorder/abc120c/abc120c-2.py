import sys
import os

# input file
f = open('testinput_c.txt', 'r')
sys.stdin = f

Ss = input()

num0 = Ss.count('0')
num1 = len(Ss) - num0

print(min(num0, num1) * 2)
