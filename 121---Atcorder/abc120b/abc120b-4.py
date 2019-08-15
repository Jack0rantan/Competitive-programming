import sys
import os

# input file
f = open('testinput.txt', 'r')
sys.stdin = f

A,B,K=map(int,input().split(' '))
print([i for i in range(max(A,B),0,-1) if A%i==B%i==0][K-1])
