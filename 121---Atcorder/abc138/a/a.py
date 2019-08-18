import sys

f = open('input.txt','r')
sys.stdin = f

n = int(input())
s = input()

if n < 3200:
    print('red')
else:
    print(s)
