import sys
import os

# input file
f = open('testinput.txt', 'r')
sys.stdin = f

a,b,c=map(int,input().split())
n=a
while c:
    if a%n==b%n==0:
        c-=1
    n-=1
print(n+1)
