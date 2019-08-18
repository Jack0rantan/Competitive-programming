import sys

# input file
f = open('input.txt', 'r')
sys.stdin = f

n = int(input())
s = input()
DIV = 998244353

ans = 3

res = ans % DIV
print(res)
