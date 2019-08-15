import sys

# input file
f = open('testinput_c.txt', 'r')
sys.stdin = f

k,x=map(int,input().split());print(*range(x-k+1,x+k))
