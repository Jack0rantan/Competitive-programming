import sys

# input file
f = open('testinput_b.txt', 'r')
sys.stdin = f

K,X = map(int,input().split())
print(*[x for x in range(X-K+1,X+K,1)])
