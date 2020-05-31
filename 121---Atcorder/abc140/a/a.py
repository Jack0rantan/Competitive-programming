import sys

f = open('input.txt','r')
sys.stdin = f

print(int(input()) ** 3)
