import sys
import os

# input file
f = open('testinput_c.txt', 'r')
sys.stdin = f

s=input().count;print(min(s('0'),s('1'))*2)
