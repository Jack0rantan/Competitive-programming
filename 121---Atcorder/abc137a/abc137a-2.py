import sys

# input file
f = open('testinput_a.txt', 'r')
sys.stdin = f

a,b=map(int,input().split());print(max(a*b,a+b,a-b))
